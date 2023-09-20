
def get_request(credentials, query, url):
    
    import requests

    auth = {
        "ST-App-Key": credentials["APP_KEY"],
        "Authorization": credentials["ACCESS_TOKEN"]
    }

    default_query_parameters = {
    }
    if query != None:
        for request in query:
            default_query_parameters[request] = query[request]
    try:
        request = requests.get(url=url,params=default_query_parameters, headers=auth)
        return request.json()
    except Exception as e:
        print(f"There was an error getting data from {url}")
        print(e)

def get(credentials, endpoint, query, id, *args, **kwargs):

    general_urls = {
        "url": "https://api.servicetitan.io/",
        "jpm_url": "https://api.servicetitan.io/jpm/v2/",
        "jpm_url_tenant": f"https://api.servicetitan.io/jpm/v2/tenant/{credentials['TENANT_ID']}",
        "accounting_url_tenant": f"https://api.servicetitan.io/accounting/v2/tenant/{credentials['TENANT_ID']}/",
    }

    # --------- ENDPOINT GROUPS --------- #

    # Accounting
    accounting_endpoints = [
        'export/inventory-bills',
        'export/invoice-items',
        'export/invoices',
        'export/payments',
        'ap-credits',
        'ap-payments',
        'inventory-bills',
        'invoices',
        'journal-entries',
        'payments',
        'payment-terms',
        'tax-zones',
    ]
    accounting_id_endpoints = [
        'journal-entries-details/',
        'journal-entries-summary/',
        'payment-types/',
    ]

    # --------- AVAILABLE ENDPOINTS --------- #

    available_endpoints = [
        'jobs',
    ]
    available_endpoint_groups = [
        accounting_endpoints,
        accounting_id_endpoints,
    ]
    for group in available_endpoint_groups:
        available_endpoints.extend(group)

    # --------- ENDPOINT TESTS --------- #

    # Tests if endpoint has been manually added or not.
    if endpoint in available_endpoints:

        # Accounting Endpoints

        if endpoint in accounting_endpoints:
            url = f"{general_urls['accounting_url_tenant']}{endpoint}"
            return get_request(credentials, query, url)

        if endpoint in accounting_id_endpoints:
            if endpoint == 'journal-entries-details/':
                if id != None:
                    url = f"{general_urls['accounting_url_tenant']}journal-entries/{id}/details"
                    return get_request(credentials,query,url)
                else:
                    print("The requested endpoint requires an ID in order to run. Please enter id as an arg.")
            if endpoint == 'journal-entries-summary/':
                if id != None:
                    url = f"{general_urls['accounting_url_tenant']}journal-entries/{id}/summary"
                    return get_request(credentials,query,url)
                else:
                    print("The requested endpoint requires an ID in order to run. Please enter id as an arg.")
            if endpoint == 'payment-types/':
                if id != None:
                    url = f"{general_urls['accounting_url_tenant']}payment-types/{id}"
                    return get_request(credentials,query,url)
                else:
                    print("The requested endpoint requires an ID in order to run. Please enter id as an arg.")

        # jobs
        if endpoint == 'jobs':
            url = f"{general_urls['jpm_url_tenant']}/jobs"
            return get_request(credentials, query, url)


    # Attempts to make a request to a general endpoint if it has not been manually added
    # TO-DO AI assisted url creation
    else:
        try:
            url = f"https://api.servicetitan.io/jpm/v2/tenant/{credentials['TENANT_ID']}/{endpoint}"
            return get_request(credentials, query, url)
        except Exception as e:
            print(f"There was an error getting data from {endpoint}. The endpoint was not found in our current available\
                  endpoint list and could not be interpretted automatically. Please submit a request for this endpoint.")
            print(e)


    # --------------------------------- Endpoint List ---------------------------------
    # ---- Accounting ----
    # export/inventory-bills
    # export/invoice-items
    # export/invoices
    # export/payments
    # ap-credits
    # ap-payments
    # inventory-bills
    # invoices
    # journal-entries
    # journal-entries/details
    # journal-entires/summary
    # payments
    # payment-terms
    # payment-terms/
    # payment-types
    # payment-types/
    # tax-zones
    # ---- CRM ----
    # export/bookings
    # export/customers
    # export/customers-contacts
    # export/leads
    # export/locations
    # export/locations-contacts
    # booking-provider-tags
    # booking-provider-tags/
    # /bookings
    # /bookings/
    # /bookings-contacts
    # bookings/
    # bookings-contacts
    # customers
    # customers-contacts
    # customers/
    # customers-contacts/
    # customers-notes/
    # leads
    # leads/
    # leads-notes/
    # locations
    # locations-contacts/
    # locations-notes/
    # ---- Dispatch ----
    # export/appointment-assignments
    # appointment-assignments
    # non-job-appointments
    # non-job-appointments/
    # teams
    # teams/
    # technician-shifts
    # technician-shifts/
    # zones
    # zones/
    # ---- Equipment Systems ----
    # installed-equipment
    # installed-equipment/
    # ---- Forms ----
    # forms
    # submissions
    # ---- Inventory ----
    # export/purchase-orders
    # adjustments
    # purchase-orders
    # purchase-orders/
    # purchase-order-markups
    # purchase-order-markups/
    # purchase-order-types
    # receipts
    # returns
    # transfers
    # trucks
    # vendors
    # vendors/
    # warehouses
    # ---- Job Booking ----
    # call-reasons
    # ---- Job Planning and Management ----
    # export/appointments
    # export/job-canceled-logs
    # export/jobs
    # export/projects
    # appointments
    # appointments/
    # job-cancel-reasons
    # job-hold-reasons
    # jobs-cancel-reasons?ids=
    # jobs
    # jobs/
    # jobs-history/
    # jobs-notes/
    # job-types
    # job-types/
    # projects
    # projects/
    # projects-notes/
    # project-statuses
    # project-statuses/
    # project-substatuses
    # project-substatuses/
    # ---- Marketing ----
    # categories
    # categories/
    # costs
    # costs/
    # campaigns
    # campaigns/
    # campaigns-costs/
    # supressions
    # suppresions/
    # ---- Marketing Reputation ----
    # reviews
    # ---- Memberships ----
    # export/invoice-templates
    # export/membership-types
    # export/memberships
    # export/recurring-service-events
    # export/recurring-service-types
    # export/recurring-services
    # memberships
    # memberships/
    # memberships-status-changes/
    # invoice-templates/
    # invoice-templates?ids=/
    # recurring-service-events
    # recurring-services
    # recurring-services/
    # membership-types
    # membership-types/
    # membership-types-discounts/
    # membership-types-duration-billing-items/
    # membership-types-recurring-service-items/
    # recurring-service-types
    # recurring-service-types/
    # ---- Payroll ----
    # export/activity-codes
    # export/gross-pay-items
    # export/jobs/splits
    # export/jobs/timesheets
    # export/payroll-adjustments
    # export/timesheet-codes
    # activity-codes
    # activity-codes/
    # gross-pay-items
    # jobs-splits
    # jobs-splits/
    # locations-rates
    # payroll-adjustments
    # payroll-adjustments/
    # employees-payrolls/
    # payrolls
    # technician-payrolls/
    # timesheet-codes
    # timesheet-codes/
    # jobs-timesheets
    # jobs-timesheets/
    # non-job-timesheets
    # ---- Pricebook ----
    # categories
    # categories/
    # discounts-and-fees
    # discounts-and-fees/
    # equipment
    # equipment/
    # images
    # materials
    # materials/
    # materialsmarkup
    # materialsmarkup/
    # services
    # services/
    # ---- Reporting ----
    # dynamic-value-sets/
    # report-categories
    # reports
    # reports/
    # ---- Sales & Estimates ----
    # estimates
    # estimates-items
    # estimates/
    # estimates-export
    # ---- Service Agreements ----
    # export/service-agreements
    # service-agreements
    # service-agreements/
    # ---- Settings ----
    # export/business-units
    # export/employees
    # export/tag-types
    # export/technicians
    # business-units
    # business-units/
    # employees
    # employees/
    # tag-types
    # technicians
    # technicians/
    # user-roles
    # ---- Task Management ----
    # data
    # ---- Telecom ----
    # export/calls
    # calls/
    # call-recording/
    # call-voicemail/
    # calls