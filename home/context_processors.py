from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist

def hasGroup(user, groupName):
    try:
        group = Group.objects.get(name=groupName)
        return group in user.groups.all()
    except ObjectDoesNotExist:
        return False  # Return False if the group does not exist

def menu_processor(request):
    menu = {}
    user = request.user
    if user.is_authenticated:  # Ensure the user is authenticated
        if hasGroup(user, 'doctor'):
            menu['Appointments'] = '/appointments'
            menu['Cases'] = '/case'
        elif hasGroup(user, 'patient'):
            menu['Reports'] = '/reports'
            menu['Appointments'] = '/appointments'
            menu['Medication'] = '/bill/medicines'
            menu['Bills'] = '/bill'
            menu['Cases'] = '/case'
        elif hasGroup(user, 'receptionist'):
            menu['New Patient'] = '/profile/register'
            menu['Manage Appointments'] = '/appointments'
            menu['New Appointment'] = '/appointments/book'
            menu['Bills'] = '/bill'
            menu['Cases'] = '/case'
            menu['Generate Case'] = '/case/generate'
        elif hasGroup(user, 'lab_attendant'):
            menu['Reports'] = '/reports'
            menu['Generate Report'] = '/reports/generate'
        elif hasGroup(user, 'inventory_manager'):
            menu['All Stock'] = ''
            menu['Stock Details'] = ''

    return {'menu': menu}
