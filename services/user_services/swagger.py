from drf_yasg import openapi
from rest_framework import status


register_user_manual_parameters = [
                openapi.Parameter('first_name', openapi.IN_FORM, type=openapi.TYPE_STRING, description='First name of User '),
                openapi.Parameter('last_name', openapi.IN_FORM, type=openapi.TYPE_STRING, description='Last name of User '),
                openapi.Parameter('email', openapi.IN_FORM, type=openapi.TYPE_STRING, format='email', description='Email of User '),
                openapi.Parameter('phone_number', openapi.IN_FORM, type=openapi.TYPE_STRING, description='Phone Number of User '),
                openapi.Parameter('password', openapi.IN_FORM, type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD, description='Password of User '),
                openapi.Parameter('user_bio', openapi.IN_FORM, type=openapi.TYPE_STRING, description='User bio '),
                openapi.Parameter('user_profile_image', openapi.IN_FORM, type=openapi.TYPE_FILE, description='Upload User profile image'),
]

register_user_responses={
                status.HTTP_200_OK: openapi.Response(
                    'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                        '_id': openapi.Schema(type=openapi.TYPE_STRING, description='Document ID'),
                        'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First Name'),
                        'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last Name'),
                        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'),
                        'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone Number'),
                        'user_profile_image_thumbnail': openapi.Schema(type=openapi.TYPE_STRING, description='URL of the thumbnail of profile image')
                    })
                )
}

login_user_manual_parameters = [
                openapi.Parameter('email', openapi.IN_FORM, type=openapi.TYPE_STRING, format='email', description='Email of User '),
                openapi.Parameter('password', openapi.IN_FORM, type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD, description='Password of User '),
]

login_user_responses={
                status.HTTP_200_OK: openapi.Response(
                    'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                        'token': openapi.Schema(type=openapi.TYPE_STRING, description='JWT Token'),
                        'user': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                             '_id': openapi.Schema(type=openapi.TYPE_STRING, description='Document ID'),
                             'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First Name'),
                             'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last Name'),
                             'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'),
                             'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone Number'),
                             'user_profile_image': openapi.Schema(type=openapi.TYPE_STRING, description='URL of the profile image')
                        })
                    })
                )
}


logout_user_manual_parameters = [
                openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING, description='Bearer Token ', required=True),
]


logout_user_responses={
                status.HTTP_200_OK: openapi.Response(
                    'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING, description='successfully logged out message')
                    })
                )
}


categories_list_user_manual_parameters = [
                openapi.Parameter('search', openapi.IN_FORM, type=openapi.TYPE_STRING, description='To search for any particular category ')
]

categories_list_user_responses={
                status.HTTP_200_OK: openapi.Response(
                    'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                        'categories': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_OBJECT, properties={
                             '_id': openapi.Schema(type=openapi.TYPE_STRING, description='Document ID'),
                             'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name'),
                             'description': openapi.Schema(type=openapi.TYPE_STRING, description='Description'),
                             'status': openapi.Schema(type=openapi.TYPE_NUMBER, description='Status'),
                             'created_at': openapi.Schema(type=openapi.TYPE_STRING, description='Created At'),
                             'updated_at': openapi.Schema(type=openapi.TYPE_STRING, description='Updated At'),
                             'added_by': openapi.Schema(type=openapi.TYPE_STRING, description='Admin ID')
                        }
                        ),
                        description='List of categories')
                    }
                    )
                )
}


header_parameters = [
    openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING, description='Token ', required=True),
]

products_list_user_manual_parameters = [
                openapi.Parameter('search', openapi.IN_FORM, type=openapi.TYPE_STRING, description='To search for any particular product ')
]

products_list_user_responses={
                status.HTTP_200_OK: openapi.Response(
                    'Success', schema= openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_OBJECT, properties={
                             '_id': openapi.Schema(type=openapi.TYPE_STRING, description='Document ID'),
                             'category_id': openapi.Schema(type=openapi.TYPE_STRING, description='Category ID'),
                             'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name'),
                             'description': openapi.Schema(type=openapi.TYPE_STRING, description='Description'),
                             'status': openapi.Schema(type=openapi.TYPE_NUMBER, description='Status'),
                             'created_at': openapi.Schema(type=openapi.TYPE_STRING, description='Created At'),
                             'updated_at': openapi.Schema(type=openapi.TYPE_STRING, description='Updated At'),
                             'added_by': openapi.Schema(type=openapi.TYPE_STRING, description='Admin ID')
                        }
                        ),
                        description='List of categories')
                    )
}


add_to_cart_manual_parameters = [
                openapi.Parameter('product_id', openapi.IN_FORM, type=openapi.TYPE_STRING, description='First name of User '),
                openapi.Parameter('quantity', openapi.IN_FORM, type=openapi.TYPE_STRING, description='Last name of User '),
                openapi.Parameter('email', openapi.IN_FORM, type=openapi.TYPE_STRING, format='email', description='Email of User '),
                openapi.Parameter('phone_number', openapi.IN_FORM, type=openapi.TYPE_STRING, description='Phone Number of User '),
                openapi.Parameter('password', openapi.IN_FORM, type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD, description='Password of User '),
                openapi.Parameter('user_bio', openapi.IN_FORM, type=openapi.TYPE_STRING, description='User bio '),
                openapi.Parameter('user_profile_image', openapi.IN_FORM, type=openapi.TYPE_FILE, description='Upload User profile image'),
]

add_to_cart_responses={
                status.HTTP_200_OK: openapi.Response(
                    'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                        '_id': openapi.Schema(type=openapi.TYPE_STRING, description='Document ID'),
                        'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First Name'),
                        'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last Name'),
                        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'),
                        'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone Number'),
                        'user_profile_image_thumbnail': openapi.Schema(type=openapi.TYPE_STRING, description='URL of the thumbnail of profile image')
                    })
                )
}


'''
{
    "product_id":"6bcf77c3-3f53-41af-b306-78aa77fee219",
    "quantity":2
}'''