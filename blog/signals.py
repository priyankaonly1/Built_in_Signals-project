from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete

@receiver(user_logged_in,sender=User)
def login_success(sender, request, user, **kwargs):
    print("------------------------------------------------------")
    print("Logged-in Signal......Run Intro")
    print("Sender:",sender)
    print("Request:", request)
    print("User:", user)
    print("User Password:", user.password)
    print(f'kwargs:{kwargs}')

@receiver(user_logged_out,sender=User)
def log_out(sender, request, user, **kwargs):
    print("-------------------------------------------------------")
    print('Logged-out Signal.......Run Outro')
    print('Sender:', sender)
    print('Request:', request)
    print('User:', user)
    print(f'kwargs:{kwargs}')

@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print('---------------------------------------------------------')
    print('Login Failed Signal')
    print('Sender:', sender)
    print('Credentials:', credentials)
    print('Request:', request)
    print(f'kwargs:{kwargs}')

@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print('-----------------------------------------------------------')
    print('Pre Save Signal........')
    print('Sender:', sender)
    print('Instance:', instance)
    print(f'kwargs:{kwargs}')

@receiver(post_save, sender=User)
def at_ending_save(sender,instance,created, **kwargs):
    if created:
        print('--------------------------------------------------------')
        print('Post Save Signal')
        print('New Record')
        print('sender:', sender)
        print('Instance:', instance)
        print('Created:', created)
        print(f'kwargs:{kwargs}')

    else:
        print('--------------------------------------------------------')
        print('Post Save Signal')
        print('Update')
        print('sender:', sender)
        print('Instance:', instance)
        print('Created:', created)
        print(f'kwargs:{kwargs}')

@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    print('--------------------------------------------------------')
    print('Pre Delete Signal')
    print('sender:', sender)
    print('Instance:', instance)
    print(f'kwargs:{kwargs}')

@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
    print('--------------------------------------------------------')
    print('Post Delete Signal')
    print('sender:', sender)
    print('Instance:', instance)
    print(f'kwargs:{kwargs}')

@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    print('--------------------------------------------------------')
    print('Pre init Signal....')
    print('sender:', sender)
    print(f'Args:{args}')
    print(f'kwargs:{kwargs}')

@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
    print('--------------------------------------------------------')
    print('Post init Signal....')
    print('sender:', sender)
    print(f'Args:{args}')
    print(f'kwargs:{kwargs}')

