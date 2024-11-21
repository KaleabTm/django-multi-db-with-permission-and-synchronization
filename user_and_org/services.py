from .models import Users,UsersOrgs,Organizations

def create_users(
        *,
        first_name=str,
        last_name=str,
        email=str,
        password=str,
        phone_number=str, 
        is_active=bool,      
    )-> Users:
    user = Users.objects.create(

        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        phone_number=phone_number,
        is_active=True,
    )

    user.full_clean()

    user.save()
    
    return user




def user_org_relation(
        *,
        user=str,
        organization=str,
        position=str,
        is_active=bool,
)-> UsersOrgs:
    org=Organizations.objects.get(org_name=organization.name)
    u = Users.objects.get(email=user.email)
    personel = UsersOrgs.objects.create(
        user=u,
        organization=org,
        position=position,
        is_active=True 
    )

    personel.full_clean()

    personel.save()