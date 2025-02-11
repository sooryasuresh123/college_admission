from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Department,Program,Student,TransferCertificate,Scholarship,StudentScholarship,User,QualifiedMark
from .forms import DepartmentForm,ProgramForm,StudentForm, TransferCertificateForm,ScholarshipForm,StudentScholarshipForm,UserForm,QualifiedMarkForm
from django.contrib import messages
from django.contrib.auth import authenticate, login


def index(request):
    return render(request,"index.html")


def manage_department(request):
    departments = Department.objects.all()
    return render(request, 'manage_department.html', {'departments': departments})

def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_department')
    else:
        form = DepartmentForm()
    return render(request, 'add_department.html', {'form': form})

def edit_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('manage_department')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'edit_department.html', {'form': form})

def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('manage_department')
    return render(request, 'delete_department.html', {'department': department})


def manage_program(request):
   programs = Program.objects.all()
   return render(request, 'manage_program.html', {'programs': programs})

def add_program(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_program')
    else:
        form = ProgramForm()
    return render(request, 'add_program.html', {'form': form})

def edit_program(request, pk):
    program = get_object_or_404(Program, id=pk)
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('manage_program')
    else:
        form =ProgramForm(instance=program)
    return render(request, 'edit_program.html', {'form': form,'program': program})

def delete_program(request, pk):
   program = get_object_or_404(Program,id=pk)
   if request.method == 'POST':
        program.delete()
        return redirect('manage_program')
   return render(request, 'delete_program.html', {'program': program})

def manage_student(request):
    students = Student.objects.all()
    return render(request, 'manage_student.html', {'students': students})
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("manage_student")  # Change this to your student listing page
    else:
        form = StudentForm()

    return render(request, "add_student.html", {"form": form})
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("manage_student")  # Redirect to student list
    else:
        form = StudentForm(instance=student)

    return render(request, "edit_student.html", {"form": form})

def delete_student(request, pk):
   student = get_object_or_404(Student, pk=pk)
   if request.method == 'POST':
        student.delete()
        return redirect('manage_student')
   return render(request, 'delete_student.html', {'student': student})


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_superuser:
                
                return redirect('index')  # Redirect to home page or dashboard
        else:
            messages.error(request, "Invalid credentials")
    
    return render(request, 'login.html')

def transfer_certificate_list(request):
    tc_list = TransferCertificate.objects.all()
    return render(request, 'transfer_certificate_list.html', {'tc_list': tc_list})

def add_transfer_certificate(request):
    if request.method == 'POST':
        form = TransferCertificateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transfer_certificate_list')
    else:
        form = TransferCertificateForm()
    return render(request, 'add_transfer_certificate.html', {'form': form})
def edit_transfer_certificate(request, tc_id):
    tc = get_object_or_404(TransferCertificate, id=tc_id)
    
    if request.method == 'POST':
        form = TransferCertificateForm(request.POST, instance=tc)
        if form.is_valid():
            form.save()
            messages.success(request, "Transfer Certificate updated successfully!")
            return redirect('transfer_certificate_list')  # Redirect to TC list page
    else:
        form = TransferCertificateForm(instance=tc)

    return render(request, 'edit_transfer_certificate.html', {'form': form, 'tc': tc})
def delete_transfer_certificate(request, tc_id):
    tc = get_object_or_404(TransferCertificate, id=tc_id)
    
    if request.method == 'POST':
        tc.delete()
        messages.success(request, "Transfer Certificate deleted successfully!")
        return redirect('transfer_certificate_list')  # Redirect to TC list page
    
    return render(request, 'confirm_delete.html', {'tc': tc})



def manage_scholarships(request):
    scholarships = Scholarship.objects.all()
    return render(request, 'manage_scholarships.html')
def scholarship_details(request):
    scholarships = Scholarship.objects.all()
    return render(request, 'scholarship_details.html', {'scholarships': scholarships})

# Add Scholarship
def add_scholarship(request):
    if request.method == 'POST':
        form = ScholarshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scholarship_details')
    else:
        form = ScholarshipForm()
    return render(request, 'add_scholarship.html', {'form': form})
def edit_scholarship(request, scholarship_id):
    scholarship = get_object_or_404(Scholarship, id=scholarship_id)
    if request.method == 'POST':
        form = ScholarshipForm(request.POST, instance=scholarship)
        if form.is_valid():
            form.save()
            return redirect('scholarship_details')
    else:
        form = ScholarshipForm(instance=scholarship)
    return render(request, 'edit_scholarship.html', {'form': form})

def delete_scholarship(request, scholarship_id):
    scholarship = get_object_or_404(Scholarship, id=scholarship_id)
    scholarship.delete()
    return redirect('scholarship_details')

def student_scholarships(request):
    student_scholarships = StudentScholarship.objects.all()
    return render(request, 'student_scholarships.html', {'student_scholarships': student_scholarships})

# Add Student Scholarship
def add_student_scholarship(request):
    if request.method == 'POST':
        form = StudentScholarshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_scholarships')
    else:
        form = StudentScholarshipForm()
    return render(request, 'add_student_scholarship.html', {'form': form})
def edit_student_scholarship(request, student_scholarship_id):
    student_scholarship = get_object_or_404(StudentScholarship, id=student_scholarship_id)
    if request.method == 'POST':
        form = StudentScholarshipForm(request.POST, instance=student_scholarship)
        if form.is_valid():
            form.save()
            return redirect('student_scholarships')
    else:
        form = StudentScholarshipForm(instance=student_scholarship)
    return render(request, 'edit_student_scholarship.html', {'form': form})

def delete_student_scholarship(request, student_scholarship_id):
    student_scholarship = get_object_or_404(StudentScholarship, id=student_scholarship_id)
    student_scholarship.delete()
    return redirect('student_scholarships')




def manage_users(request):
    users = User.objects.all()
    return render(request, 'manage_users.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_users')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('manage_users')
    else:
        form = UserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form})

def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('manage_users')
    return render(request, 'delete_user.html', {'user': user})

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

# @login_required
# def dashboard(request):
#     user = request.user
    
#     if user.is_student():
#         return render(request, 'dashboard.html')
    
#     elif user.is_office_admin():
#         return render(request, 'dashboard.html')
    
#     elif user.is_principal():
#         return render(request, 'dashboard.html')
    
#     else:
#         return redirect('login')  # Redirect to login if no role found
def manage_qualified_marks(request):
    qualified_marks = QualifiedMark.objects.select_related('stud','board').all()
    return render(request, 'manage_qualified_marks.html', {'qualified_marks': qualified_marks})

def add_qualified_mark(request):
    if request.method == 'POST':
        form = QualifiedMarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_qualified_marks')
    else:
        form = QualifiedMarkForm()
    return render(request, 'add_qualified_mark.html', {'form': form})

def edit_qualified_mark(request, stud_id):
    qualified_mark = get_object_or_404(QualifiedMark, stud_id=stud_id)
    if request.method == 'POST':
        form = QualifiedMarkForm(request.POST, instance=qualified_mark)
        if form.is_valid():
            form.save()
            return redirect('manage_qualified_marks')
    else:
        form = QualifiedMarkForm(instance=qualified_mark)
    return render(request, 'edit_qualified_mark.html', {'form': form})

def delete_qualified_mark(request, stud_id):
    qualified_mark = get_object_or_404(QualifiedMark, stud_id=stud_id)
    
    if request.method == 'POST':
        qualified_mark.delete()
        return redirect('manage_qualified_marks')

    return render(request, 'delete_qualified_mark.html', {'qualified_mark': qualified_mark})
