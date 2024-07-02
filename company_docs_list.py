# company_policies.py

def get_docs_list():
    return [
        "Detailed technical specifications for specific pump models",
        "Material compatibility information for different fluid types and temperatures",
        "Current pricing information and bulk order discounts",
        "Lead times for standard and custom equipment",
        "Recommended installation procedures and best practices",
        "Required tools and equipment for installation",
        "Recommended maintenance schedules and procedures",
        "Lubrication requirements and recommended lubricants",
        "Procedures for equipment start-up and shutdown",
        "Guidelines for equipment storage during downtime",
        "Procedures for returning equipment for factory repair",
        "Estimated repair costs and turnaround times",
        "Lead times for spare part delivery",
        "Assistance with equipment selection based on application requirements",
        "Availability of digital copies of product literature",
        "Guidance on meeting environmental regulations",
        "Requests for site visits or product demonstrations",
        "Information on retrofit kits for improved performance",
        "Support for conducting equipment health checks or audits",
    ]

# You can test the function here
if __name__ == "__main__":
    policies = get_docs_list()
    for i, policy in enumerate(policies, 1):
        print(f"{i}. {policy}")
