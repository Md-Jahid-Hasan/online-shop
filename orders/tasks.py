from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    order.first_name = "Mahin"
    order.save()
    print("Mail sent work")
    subject = f'Order No. {order.id}'
    message = f'Dear {order.first_name}, \n\n' \
        f'You have successfully placed and order.' \
        f'your order Id id {order.id}.'
    mail_sent = send_mail(subject, message, 'admin@gmail.com', [order.email])

    return mail_sent
