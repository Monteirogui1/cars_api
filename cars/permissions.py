from rest_framework import permissions


class BrandPermissionClass(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('cars.view_brand')

        if request.method == 'POST':
            return request.user.has_perm('cars.add_brand')

        if request.method == ['PATCH', 'PUT']:
            return request.user.has_perm('cars.change_brand')

        if request.method == 'DELETE':
            return request.user.has_perm('cars.delete_brand')

        return False


class TypePermissionClass(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('cars.view_brand')

        if request.method == 'POST':
            return request.user.has_perm('cars.add_brand')

        if request.method == ['PATCH', 'PUT']:
            return request.user.has_perm('cars.change_brand')

        if request.method == 'DELETE':
            return request.user.has_perm('cars.delete_brand')

        return False


class CarPermissionClass(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('cars.view_car')

        if request.method == 'POST':
            return request.user.has_perm('cars.add_car')

        if request.method == ['PATCH', 'PUT']:
            return request.user.has_perm('cars.change_car')

        if request.method == 'DELETE':
            return request.user.has_perm('cars.delete_car')

        return False
