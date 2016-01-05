from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class MLHAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, 
        request, 
        sociallogin, 
        data):
        
        user = DefaultSocialAccountAdapter.populate_user(self, request, sociallogin, data)
        
        user.graduation = data.get('graduation')
        user.major = data.get('major')
        user.shirt_size = data.get('shirt_size')
        user.dietary_restrictions = data.get('dietary_restrictions')
        user.special_needs = data.get('special_needs')
        user.date_of_birth = data.get('date_of_birth')
        user.gender = data.get('gender')
        user.phone_number = data.get('phone_number')
        user.school = data.get('school')

        return user