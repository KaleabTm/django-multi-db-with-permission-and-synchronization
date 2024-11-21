# command to sync data from user_org to default db
from django.core.management.base import BaseCommand
from user_and_org.models import Organizations
from organizations.models import OurOrganizations
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
            # Fetch the organization from user_org DB
            organization = Organizations.objects.using('user_org').get(org_domain=org_domain)
        
        except Organizations.DoesNotExist:
            self.stderr.write(self.style.ERROR(f"Organization with domain {org_domain} does not exist."))
            return
        
        try:
            # Sync the data to the default database
            OurOrganizations.objects.using('default').update_or_create(
                pk=organization.pk,
                defaults={
                    'org_name': organization.org_name,
                    'org_email': organization.org_email,
                    'org_phone_no': organization.org_phone_no,
                    'org_description': organization.org_description,
                    'org_domain': organization.org_domain,
                    'postal_code': organization.postal_code,
                    'city': organization.city,
                }
            )
            self.stdout.write(self.style.SUCCESS(f"Synced organization {organization.org_name}."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error syncing organization {organization}: {str(e)}"))
