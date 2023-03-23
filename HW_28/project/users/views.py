import json

from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from users.models import User, Location


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        return JsonResponse({"id": user.id,
                             "first_name": user.first_name,
                             "last_name": user.last_name,
                             "username": user.username,
                             "location": [loc.name for loc in user.location.all()],
                             "age": user.age,
                             "role": user.role,
                             })


class UserListView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        paginator = Paginator(self.object_list, 10)
        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)


        return JsonResponse([{"id": user.id,
                              "first_name": user.first_name,
                              "last_name": user.last_name,
                              "username": user.username,
                              "location": [loc.name for loc in user.location.all()],
                              "age": user.age,
                              "role": user.role,
                              "total_ads": user.total_ads} for user in
                             self.object_list.annotate(total_ads=Count("ad", filter=Q(ad__is_published=True)))],
                            safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        locations = data.pop('location')
        user = User.objects.create(**data)
        for loc_name in locations:
            loc, _ = Location.objects.get_or_create(name=loc_name)
            user.location.add(loc)

        return JsonResponse({"id": user.id,
                             "first_name": user.first_name,
                             "last_name": user.last_name,
                             "username": user.username,
                             "location": [loc.name for loc in user.location.all()],
                             "age": user.age,
                             "role": user.role})


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        super().delete(request, *args, **kwargs)
        return JsonResponse({"id": user.id})


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = "__all__"

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = json.loads(request.body)

        if "first_name" in data:
            self.object.first_name = data.get("first_name")
        if "last_name" in data:
            self.object.last_name = data.get("last_name")
        if "username" in data:
            self.object.username = data.get("username")
        if "age" in data:
            self.object.age = data.get("age")
        if "location" in data:
            self.object.location.all().delete()
            for loc_name in data:
                loc, _ = Location.objects.get_or_create(name=loc_name)
                self.object.location.add(loc)

        self.object.save()
        return JsonResponse({"id": self.object.id,
                             "first_name": self.object.first_name,
                             "last_name": self.object.last_name,
                             "username": self.object.username,
                             "location": [loc.name for loc in self.object.location.all()],
                             "age": self.object.age,
                             "role": self.object.role})
