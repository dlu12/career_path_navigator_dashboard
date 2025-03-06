
from django.contrib import admin
from django.urls import path

from myapp import views, rs3, ks2, ks

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login_get/',views.login_get),
    path('login_post/',views.login_post),

    path('add_college_get/',views.add_college_get),
    path('add_college_post/',views.add_college_post),

    path('add_notification_get/',views.add_notification_get),
    path('add_notification_post/',views.add_notification_post),

    path('add_skill_get/',views.add_skill_get),
    path('add_skill_post/',views.add_skill_post),
    path('change_password_get/',views.change_password_get),
    path('change_password_post/',views.change_password_post),
    path('edit_college_get/<id>',views.edit_college_get),
    path('edit_college_post/',views.edit_college_post),
    path('edit_notification_get/<id>',views.edit_notification_get),
    path('edit_notification_post/',views.edit_notification_post),
    path('send_reply_get/<id>',views.send_reply_get),
    path('send_reply_post/',views.send_reply_post),
    path('view_approved_company_get/',views.view_approved_company_get),
    path('view_approved_company_post/',views.view_approved_company_post),
    path('view_college_get/',views.view_college_get),
    path('view_college_post/',views.view_college_post),
    path('view_company_get/',views.view_company_get),
    path('view_company_post/',views.view_company_post),
    path('view_complaints_get/',views.view_complaints_get),
    path('view_complaints_post/',views.view_complaints_post),
    path('view_course_get/<id>',views.view_course_get),
    path('view_course_post/',views.view_course_post),
    path('view_notification_get/',views.view_notification_get),
    path('view_notification_post/',views.view_notification_post),
    path('view_rejected_company_get/',views.view_rejected_company_get),
    path('view_rejected_company_post/',views.view_rejected_company_post),
    path('view_vaccancy_get/<id>',views.view_vaccancy_get),
    path('view_vaccancy_post/',views.view_vaccancy_post),    path('view_vaccancy_post/',views.view_vaccancy_post),
    path('admin_home/', views.adminhome),
    path('view_skill_get/', views.view_skill_get),
    path('view_skill_post/', views.view_skill_post),
    path('delete_college/<id>', views.delete_college),
    path('delete_notification/<id>', views.delete_notification),
    path('delete_skill/<id>', views.delete_skill),
    path('approve_company/<id>', views.approve_company),
    path('reject_company/<id>', views.reject_company),



    ##########################3
    path('company_home/', views.company_home),
    path('add_vaccancy_company_get/', views.add_vaccancy_company_get),
    path('add_vaccancy_company_post/', views.add_vaccancy_company_post),
    path('company_change_password_get/', views.company_change_password_get),
    path('company_change_password_post/', views.company_change_password_post),
    path('edit_profile_get/', views.edit_profile_get),
    path('edit_profile_post/', views.edit_profile_post),
    path('edit_vaccancy_get/<id>', views.edit_vaccancy_get),
    path('edit_vaccancy_post/', views.edit_vaccancy_post),
    path('signup_company_get/', views.signup_company_get),
    path('signup_company_post/', views.signup_company_post),
    path('view_approved_request_get/', views.view_approved_request_get),
    path('view_approved_request_post/', views.view_approved_request_post),
    path('view_profile_get/', views.view_profile_get),
    path('view_rejected_request_get/', views.view_rejected_request_get),
    path('view_rejected_request_post/', views.view_rejected_request_post),
    path('view_skill_company_get/<id>', views.view_skill_company_get),
    path('view_skill_company_post/', views.view_skill_company_post),
    path('view_vaccancy_company_get/', views.view_vaccancy_company_get),
    path('view_vaccancy_company_post/', views.view_vaccancy_company_post),
    path('view_vaccancy_request_get/<id>', views.view_vaccancy_request_get),
    path('view_vaccancy_request_post/', views.view_vaccancy_request_post),
    path('approve_request_get/<id>', views.approve_request_get),
    path('reject_request_get/<id>', views.reject_request_get),
    path('delete_vaccancy_get/<id>', views.delete_vaccancy_get),
    path('view_resume/<id>', views.view_resume),
    path('add_vaccancy_company_skill_get/<id>', views.add_vaccancy_company_skill_get),
    path('add_vaccany_company_skill_post/', views.add_vaccancy_company_skill_post),


    ###college

    path('college_home/', views.college_home),
    path('add_course_get/', views.add_course_get),
    path('add_coures_post/', views.add_course_post),
    path('add_department_get/', views.add_department_get),
    path('add_department_post/', views.add_department_post),
    path('add_facility_get/', views.add_facility_get),
    path('add_facility_post/', views.add_facility_post),
    path('add_fee_get/', views.add_fee_get),
    path('add_fee_post/', views.add_fee_post),
    path('edit_course_get/<id>', views.edit_course_get),
    path('edit_course_post/', views.edit_course_post),
    path('edit_department_get/<id>', views.edit_department_get),
    path('edit_department_post/', views.edit_department_post),
    path('edit_facility_get/<id>', views.edit_facility_get),
    path('edit_facility_post/', views.edit_facility_post),
    path('edit_fee_get/<id>', views.edit_fee_get),
    path('edit_fee_post/', views.edit_fee_post),
    path('view_college_profile_get/', views.view_college_profile_get),
    path('view_course_college_get/', views.view_course_college_get),
    path('view_course_college_post/', views.view_course_college_post),
    path('view_department_get/', views.view_department_get),
    path('view_department_post/', views.view_department_post),
    path('view_facility_get/', views.view_facility_get),
    path('view_facility_post/', views.view_facility_post),
    path('view_fee_get/', views.view_fee_get),
    path('view_fee_post/', views.view_fee_post),
    path('college_change_password_get/', views.college_change_password_get),
    path('college_change_password_post/', views.college_change_password_post),

    path('delete_department/<id>', views.delete_department),
    path('delete_course/<id>', views.delete_course),
    path('delete_fee/<id>', views.delete_fee),
    path('delete_facility/<id>', views.delete_facility),

    path('logout/', views.logout),


    # ---------------------------flutter---------------------------


    path('user_login/',views.user_login),
    path('user_change_password/',views.user_change_password),
    path('user_signup/',views.user_signup),
    path('user_addownskill/',views.user_addownskill),
    path('user_viewownskill/',views.user_viewownskill),
    path('user_deleteownskill/<id>',views.user_deleteownskill),
    path('user_viewapprovedcompany/',views.user_viewapprovedcompany),
    path('user_viewvaccancy/',views.user_viewvaccancy),
    path('user_send_request/<id>',views.user_send_request),
    path('user_send_complaint/', views.user_send_complaint),
    path('user_view_reply/', views.user_view_reply),
    path('user_view_college/', views.user_view_college),
    path('user_view_course/', views.user_view_course),
    path('user_view_facility/', views.user_view_facility),
    path('user_view_fees/', views.user_view_fees),
    path('user_viewprofile/', views.user_viewprofile),
    path('user_editprofile/', views.user_editprofile),
    path('user_skill/', views.user_skill),
    path('user_View_notification_post/', views.user_View_notification_post),


    path('resume1/', rs3.create_resume),
    path('resume2/', ks2.create_resume2),
    path('resume3/', ks.create_resume3),


]
