from rest_framework import permissions


class AdminOrReadOnly(permissions.BasePermission):
    '''Запрет на редактирование и удаление контента,
     кроме администратора и супераользователя.'''

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request._user.role == 'admin'
            or request._user.is_superuser
        )


class OwnerOrReadOnly(permissions.BasePermission):
    '''Запрет на редактирование и удаление контента,
     кроме автора и модератора.'''

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.user.role == 'moderator'
        )
