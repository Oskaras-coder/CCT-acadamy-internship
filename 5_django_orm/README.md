# Task
Let’s get back to the reservations task:
review your models.py file. What changes do you think are needed?
Also, you’ve missed one important part - what if you’re reserving a meeting room, which is already taken? Implement this logic (obviously we’ll need querysets, right?)
Let’s add the `users` field to the `Reservation` model
Let’s add an abstract model for all models. What would we put there?
Also, let’s implement `transaction.atomic`. Be sure to know how does that work
Use select_related and prefetch_related at least once
Create an endpoint to get user-created reservations
Create an endpoint to get user reservations in which he’s attending

# Goals
- Viewsets (GenericViewSet, ModelViewSet, Mixins, routing)
- Serializers (Validation, working with ModelSerializer: create, update instance, overriding these methods)
- Filters

# Material
- https://www.django-rest-framework.org
