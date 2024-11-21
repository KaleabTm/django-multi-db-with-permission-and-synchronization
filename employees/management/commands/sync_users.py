from django.core.management.base import BaseCommand
from user_and_org.models import Organizations, UsersOrgs
from employees.models import Employees
from django.contrib.auth.hashers import make_password
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Command(BaseCommand):
    help = 'Sync users with organization users'

    def handle(self, *args, **options):
        # Retrieve ORG_DOMAIN from environment variables
        org_domain = os.getenv('ORG_DOMAIN')
        if not org_domain:
            self.stderr.write(self.style.ERROR("ORG_DOMAIN is not set in the environment variables."))
            return

        try:
            # Fetch the organization
            organization = Organizations.objects.get(org_domain=org_domain)
        except Organizations.DoesNotExist:
            self.stderr.write(self.style.ERROR(f"Organization with domain {org_domain} does not exist."))
            return

        # Fetch all users associated with the organization
        org_users = UsersOrgs.objects.filter(organization=organization)
        if not org_users.exists():
            self.stdout.write(self.style.WARNING(f"No users found for organization {organization.org_name}."))
            return

        # Sync each user with the Employees table
        for user_org in org_users:
            user = user_org.user
            try:
                # Retrieve or create the Employee object
                employee, created = Employees.objects.get_or_create(pk=user.pk)

                # Map fields to sync
                fields_to_sync = {
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'phone_number': user.phone_number,
                    'email': user.email,
                }

                # Update only fields that need changes
                updated_fields = []
                for field, value in fields_to_sync.items():
                    if getattr(employee, field) != value:
                        setattr(employee, field, value)
                        updated_fields.append(field)

                # Handle password separately
                if user.password and user.password != employee.password:
                    employee.password = make_password(user.password)
                    updated_fields.append('password')

                # # Set is_active to True if not already
                # if not employee.is_active:
                #     employee.is_active = True
                #     updated_fields.append('is_active')

                # Save changes if there are updates
                if updated_fields:
                    employee.save(update_fields=updated_fields)
                    self.stdout.write(self.style.SUCCESS(
                        f"Updated user {user.id} with fields: {', '.join(updated_fields)}"
                    ))
                else:
                    self.stdout.write(self.style.NOTICE(f"No updates required for user {user.id}."))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"Error syncing user {user.id}: {str(e)}"))

        self.stdout.write(self.style.SUCCESS(f"Sync completed for organization {organization.org_name}."))
