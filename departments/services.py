from django.db import transaction
from django.contrib.auth.models import Group, Permission
from django.forms import ValidationError
from departments.models import Department, JobTitle


def department_create(
    *,
    department_name: str,
    description: str,
    contact_phone: int,
    contact_email: str,
    is_active: bool
) -> Department:
    department = Department(
        department_name=department_name,
        description=description,
        contact_phone=contact_phone,
        contact_email=contact_email,
        is_active=True
    )

    department.full_clean()

    department.save()

    return department


def jobtitle_create(
        *,
        title: str,
        department: str,
        permissions: list = []
) -> JobTitle:
    # Create or get the department object
    department_instance, created = Department.objects.get_or_create(department_name=department)

    # Create the JobTitle object
    position = JobTitle(
        title=title,
        department=department_instance,
    )

    try:
        # Clean the position object (validate fields)
        position.full_clean()  # This will raise ValidationError if there are issues
    except ValidationError as e:
        raise ValueError(f"JobTitle creation failed due to validation error: {e}")

    # Start a transaction to ensure atomicity
    with transaction.atomic():
        # Create or get the group (used for permissions)
        group, created = Group.objects.get_or_create(name=title)

        # Assign permissions to the group
        if permissions:
            for perm in permissions:
                try:
                    permission = Permission.objects.get(codename=perm)
                    group.permissions.add(permission)
                except Permission.DoesNotExist:
                    raise ValueError(f"Permission '{perm}' does not exist.")
        
        # Save the group with the new permissions
        group.save()

        # Save the job title
        position.save()

    return position

