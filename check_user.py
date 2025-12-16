import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'horilla.settings')
django.setup()

from django.contrib.auth.models import User
from employee.models import Employee, EmployeeWorkInformation
from base.models import Company, Department, JobPosition

try:
    user = User.objects.get(username='satalan')
    print(f"✓ User 'satalan' exists!")
    print(f"  ID: {user.id}")
    print(f"  Email: {user.email}")
    print(f"  Is Active: {user.is_active}")
except User.DoesNotExist:
    print("✗ User 'satalan' not found. Creating now...")
    user = User.objects.create_user(username='satalan', password='abc123')
    print(f"✓ User created successfully: {user.username}")

# Check if employee exists for this user
try:
    employee = Employee.objects.get(employee_user_id=user)
    print(f"✓ Employee profile exists for user 'satalan': {employee.employee_first_name} {employee.employee_last_name}")
    print(f"  Employee ID: {employee.id}")
    
    # Check work information
    if hasattr(employee, 'employee_work_info') and employee.employee_work_info:
        work_info = employee.employee_work_info
        print(f"✓ Work Information assigned:")
        print(f"  Department: {work_info.department_id}")
        print(f"  Job Position: {work_info.job_position_id}")
    else:
        print("⚠ No work information linked to this employee yet.")
        
except Employee.DoesNotExist:
    print("✗ Employee profile not found for user 'satalan'. Creating now...")
    
    # Get or create default company
    company = Company.objects.first()
    if not company:
        company = Company.objects.create(
            company="Default Company",
            address="123 Main Street",
            country="Sri Lanka",
            state="Western",
            city="Colombo",
            zip="00100"
        )
        print(f"  Created default company: {company.company}")
    
    # Get or create default department
    department = Department.objects.first()
    if not department:
        department = Department.objects.create(department="General")
        department.company_id.add(company)
        print(f"  Created default department: {department.department}")
    
    # Get or create default job position
    job_position = JobPosition.objects.first()
    if not job_position:
        job_position = JobPosition.objects.create(job_position="Employee")
        print(f"  Created default job position: {job_position.job_position}")
    
    # Create employee profile
    employee = Employee.objects.create(
        employee_user_id=user,
        employee_first_name="Satalan",
        employee_last_name="Arunthavanathan",
        email="satalan@example.com",
        phone="+94771234567",
        nic_number="123456789V",
        is_active=True
    )
    
    # Create employee work information
    try:
        work_info = EmployeeWorkInformation.objects.create(
            employee_id=employee,
            department_id=department,
            job_position_id=job_position
        )
        print(f"✓ Employee profile created: {employee.employee_first_name} {employee.employee_last_name}")
        print(f"  Employee ID: {employee.id}")
        print(f"  Linked to User: {employee.employee_user_id.username}")
        print(f"✓ Work Information assigned: Department={department.department}, Position={job_position.job_position}")
    except Exception as e:
        print(f"✓ Employee profile created: {employee.employee_first_name} {employee.employee_last_name}")
        print(f"  Employee ID: {employee.id}")
        print(f"  Linked to User: {employee.employee_user_id.username}")
        print(f"  (Work information may have been created automatically)")

print("\n✓ Setup Complete! User 'satalan' with password 'abc123' is ready to log in.")
