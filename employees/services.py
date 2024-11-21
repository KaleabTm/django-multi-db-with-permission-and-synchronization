from .models import Employees

def create_employees(
        *,
        first_name=str,
        last_name=str,
        email=str,
        password=str,
        phone_number=str,
        position=str,
        department=str,
        is_active=bool,
        is_superuser=bool,
        is_staff=bool,


) -> Employees:
    employee=Employees.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        phone_number=phone_number,
        position=position,
        department=department,
        is_active=True,
        is_superuser=False,
        is_staff=False,
    )

    employee.full_clean()
    employee.save()

    return employee