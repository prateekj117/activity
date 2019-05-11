from .views import *

from django.urls import re_path

# place app url patterns here

urlpatterns = [
    re_path(r'^dashboard/project/(?P<pk>\w+)/$',
            ProjectDash.as_view(), name='project_dashboard'),
    re_path(r'^dashboard/project/(?P<pk>\w+)$',
            ProjectDash.as_view(), name='project_dashboard'),
    re_path(r'^dashboard/project', ProjectDash.as_view(),
            name='project_dashboard'),
    re_path(
        r'^dashboard/(?P<pk>\w+)/(?P<status>[\w ]+)/$', ProgramDash.as_view(), name='dashboard'),
    re_path(r'^dashboard/(?P<pk>\w+)/$',
            ProgramDash.as_view(), name='dashboard'),

    re_path(r'^projectagreement_list/(?P<pk>\w+)/(?P<status>[\w ]+)/$',
            ProjectAgreementList.as_view(), name='projectagreement_list'),
    re_path(r'^projectagreement_add/$',
            ProjectAgreementCreate.as_view(), name='projectagreement_add'),
    re_path(r'^projectagreement_update/(?P<pk>\w+)/$',
            ProjectAgreementUpdate.as_view(), name='projectagreement_update'),
    re_path(r'^projectagreement_delete/(?P<pk>\w+)/$',
            ProjectAgreementDelete.as_view(), name='projectagreement_delete'),
    re_path(r'^projectagreement_import',
            ProjectAgreementImport.as_view(), name='projectagreement_import'),
    re_path(r'^projectagreement_detail/(?P<pk>\w+)/$',
            ProjectAgreementDetail.as_view(), name='projectagreement_detail'),

    re_path(r'^projectcomplete_list/(?P<pk>\w+)/$',
            ProjectCompleteList.as_view(), name='projectcomplete_list'),
    re_path(r'^projectcomplete_add/(?P<pk>\w+)/$',
            ProjectCompleteCreate.as_view(), name='projectcomplete_add'),
    re_path(r'^projectcomplete_update/(?P<pk>\w+)/$',
            ProjectCompleteUpdate.as_view(), name='projectcomplete_update'),
    re_path(r'^projectcomplete_delete/(?P<pk>\w+)/$',
            ProjectCompleteDelete.as_view(), name='projectcomplete_delete'),
    re_path(r'^projectcomplete_import', ProjectCompleteImport.as_view(),
            name='projectcomplete_import'),
    re_path(r'^projectcomplete_detail/(?P<pk>\w+)/$',
            ProjectCompleteDetail.as_view(), name='projectcomplete_detail'),

    re_path(r'^siteprofile_list/(?P<program_id>\w+)/(?P<activity_id>\w+)/$',
            SiteProfileList.as_view(), name='siteprofile_list'),
    re_path(r'^siteprofile_report/(?P<pk>\w+)/$',
            SiteProfileReport.as_view(), name='siteprofile_report'),
    re_path(r'^siteprofile_add', SiteProfileCreate.as_view(),
            name='siteprofile_add'),
    re_path(r'^siteprofile_update/(?P<pk>\w+)/$',
            SiteProfileUpdate.as_view(), name='siteprofile_update'),
    re_path(r'^siteprofile_delete/(?P<pk>\w+)/$',
            SiteProfileDelete.as_view(), name='siteprofile_delete'),

    re_path(r'^site_indicatordata/(?P<site_id>\w+)/$',
            IndicatorDataBySite.as_view(), name='site_indicatordata'),
    re_path(r'^site_projectscomplete/(?P<site_id>\w+)/$',
            ProjectCompleteBySite.as_view(), name='site_projectscomplete'),
    # re_path(r'^site_projects/(?P<site_id>\w+)/$', ProjectsBySite.as_view(), name='site_projects'),

    re_path(r'^documentation_list/(?P<program>\w+)/(?P<project>\w+)/$',
            DocumentationList.as_view(), name='documentation_list'),
    re_path(r'^documentation_objects/(?P<program>\w+)/(?P<project>\w+)/$',
            DocumentationListObjects.as_view(), name='documentation_objects'),
    re_path(r'^documentation_add', DocumentationCreate.as_view(),
            name='documentation_add'),
    re_path(r'^documentation_agreement_list/(?P<program>\w+)/(?P<project>\w+)/$',
            DocumentationAgreementList.as_view(), name='documentation_agreement_list'),
    re_path(r'^documentation_agreement_add/(?P<id>\w+)/$',
            DocumentationAgreementCreate.as_view(), name='documentation_agreement_add'),
    re_path(r'^documentation_agreement_update/(?P<pk>\w+)/(?P<id>\w+)/$',
            DocumentationAgreementUpdate.as_view(), name='documentation_agreement_update'),
    re_path(r'^documentation_agreement_delete/(?P<pk>\w+)/$',
            DocumentationAgreementDelete.as_view(), name='documentation_agreement_delete'),
    re_path(r'^documentation_update/(?P<pk>\w+)/$',
            DocumentationUpdate.as_view(), name='documentation_update'),
    re_path(r'^documentation_delete/(?P<pk>\w+)/$',
            DocumentationDelete.as_view(), name='documentation_delete'),

    re_path(r'^monitor_list/(?P<pk>\w+)/$',
            MonitorList.as_view(), name='monitor_list'),
    re_path(r'^monitor_add/(?P<id>\w+)/$',
            MonitorCreate.as_view(), name='monitor_add'),
    re_path(r'^monitor_update/(?P<pk>\w+)/$',
            MonitorUpdate.as_view(), name='monitor_update'),
    re_path(r'^monitor_delete/(?P<pk>\w+)/$',
            MonitorDelete.as_view(), name='monitor_delete'),

    re_path(r'^quantitative_add/(?P<id>\w+)/$',
            QuantitativeOutputsCreate.as_view(), name='quantitative_add'),
    re_path(r'^quantitative_update/(?P<pk>\w+)/$',
            QuantitativeOutputsUpdate.as_view(), name='quantitative_update'),
    re_path(r'^quantitative_delete/(?P<pk>\w+)/$',
            QuantitativeOutputsDelete.as_view(), name='quantitative_delete'),

    re_path(r'^benchmark_add/(?P<id>\w+)/$',
            BenchmarkCreate.as_view(), name='benchmark_add'),
    re_path(r'^benchmark_update/(?P<pk>\w+)/$',
            BenchmarkUpdate.as_view(), name='benchmark_update'),
    re_path(r'^benchmark_delete/(?P<pk>\w+)/$',
            BenchmarkDelete.as_view(), name='benchmark_delete'),

    # urls for projectcomplete version of popup
    re_path(r'^benchmark_complete_add/(?P<id>\w+)/$',
            BenchmarkCreate.as_view(), name='benchmark_add'),
    re_path(r'^benchmark_complete_update/(?P<pk>\w+)/$',
            BenchmarkUpdate.as_view(), name='benchmark_update'),
    re_path(r'^benchmark_complete_delete/(?P<pk>\w+)/$',
            BenchmarkDelete.as_view(), name='benchmark_delete'),

    re_path(r'^stakeholder_list/(?P<program_id>\w+)/(?P<pk>\w+)/$',
            StakeholderList.as_view(), name='stakeholder_list'),

    re_path(r'^stakeholder_table/(?P<program_id>\w+)/(?P<pk>\w+)/$',
            StakeholderObjects.as_view(), name='stakeholder_table'),

    re_path(r'^stakeholder_add/(?P<id>\w+)/$',
            StakeholderCreate.as_view(), name='stakeholder_add'),
    re_path(r'^stakeholder_update/(?P<pk>\w+)/$',
            StakeholderUpdate.as_view(), name='stakeholder_update'),
    re_path(r'^stakeholder_delete/(?P<pk>\w+)/$',
            StakeholderDelete.as_view(), name='stakeholder_delete'),
    re_path(r'^export_stakeholders_list/(?P<program_id>\w+)/$',
            export_stakeholders_list, name='export_stakeholders_list'),

    re_path(r'^site_list/(?P<program_id>\w+)/(?P<pk>\w+)/$',
            SiteProfileList.as_view(), name='site_list'),

    re_path(r'^site_table/(?P<program_id>\w+)/(?P<pk>\w+)/$',
            SiteProfileObjects.as_view(), name='site_table'),

    re_path(r'^site_add/(?P<id>\w+)/$',
            SiteProfileCreate.as_view(), name='site_add'),
    re_path(r'^site_update/(?P<pk>\w+)/$',
            SiteProfileUpdate.as_view(), name='site_update'),
    re_path(r'^site_delete/(?P<pk>\w+)/$',
            SiteProfileDelete.as_view(), name='site_delete'),
    re_path(r'^export_sites_list/(?P<program_id>\w+)/$',
            export_sites_list, name='export_sites_list'),

    re_path(r'^contact_list/(?P<pk>\w+)/$',
            ContactList.as_view(), name='contact_list'),
    re_path(r'^contact_add/(?P<stakeholder_id>\w+)/(?P<id>\w+)/$',
            ContactCreate.as_view(), name='contact_add'),
    re_path(r'^contact_update/(?P<stakeholder_id>\w+)/(?P<pk>\w+)/$',
            ContactUpdate.as_view(), name='contact_update'),
    re_path(r'^contact_delete/(?P<pk>\w+)/$',
            ContactDelete.as_view(), name='contact_delete'),

    re_path(r'^checklistitem_list/(?P<pk>\w+)/$',
            ChecklistItemList.as_view(), name='checklistitem_list'),
    re_path(r'^checklistitem_add/(?P<id>\w+)/$',
            ChecklistItemCreate.as_view(), name='checklistitem_add'),
    re_path(r'^checklistitem_update/(?P<pk>\w+)/$',
            ChecklistItemUpdate.as_view(), name='checklistitem_update'),
    re_path(r'^checklist_update_link/(?P<pk>\w+)/(?P<type>\w+)/(?P<value>\w+)/$',
            checklist_update_link, name='checklist_update_link'),
    re_path(r'^checklistitem_delete/(?P<pk>\w+)/$',
            ChecklistItemDelete.as_view(), name='checklistitem_delete'),

    re_path(r'^budget_list/(?P<pk>\w+)/$',
            BudgetList.as_view(), name='budget_list'),
    re_path(r'^budget_add/(?P<id>\w+)/$',
            BudgetCreate.as_view(), name='budget_add'),
    re_path(r'^budget_update/(?P<pk>\w+)/$',
            BudgetUpdate.as_view(), name='budget_update'),
    re_path(r'^budget_delete/(?P<pk>\w+)/$',
            BudgetDelete.as_view(), name='budget_delete'),

    re_path(r'^report/export/$', Report.as_view(), name='report'),
    re_path(
        r'^report/(?P<pk>\w+)/(?P<status>[\w ]+)/$', Report.as_view(), name='report'),
    re_path(
        r'^report_table/(?P<pk>\w+)/(?P<status>[\w ]+)/$', ReportData.as_view(), name='report_data'),
    re_path(r'^export_stakeholders_list/', export_stakeholders_list,
            name='export_stakeholders_list'),
    re_path(r'^export_sites_list/', export_sites_list,
            name='export_sites_list'),

    re_path(r'^province/(?P<province>[-\w]+)/province_json/',
            province_json, name='province_json'),
    re_path(r'^country/(?P<country>[-\w]+)/country_json/',
            country_json, name='country_json'),
    re_path(r'^district/(?P<district>[-\w]+)/district_json/',
            district_json, name='district_json'),

    # ajax calls
    re_path(r'^service/(?P<service>[-\w]+)/service_json/',
            service_json, name='service_json'),
    re_path(r'^new_bookmark/$', save_bookmark, name='save_bookmark'),

]