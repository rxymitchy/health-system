from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Program, Client, Enrollment, db
from datetime import datetime
from app.forms import ProgramForm, ClientForm, EnrollmentForm

main = Blueprint('main', __name__)


@main.route('/')
def index():
    try:
        program_count = Program.query.count()
        client_count = Client.query.count()
        enrollment_count = Enrollment.query.filter_by(is_active=True).count()
    except:
        # Handle case when tables don't exist yet
        program_count = 0
        client_count = 0
        enrollment_count = 0
    
    return render_template('index.html',
                         program_count=program_count,
                         client_count=client_count,
                         enrollment_count=enrollment_count)



@main.route('/programs', methods=['GET', 'POST'])
def programs():
    form = ProgramForm()
    if form.validate_on_submit():
        program = Program(name=form.name.data)
        db.session.add(program)
        db.session.commit()
        flash('Program added successfully!', 'success')
        return redirect(url_for('main.programs'))
    
    programs = Program.query.all()
    return render_template('programs.html', form=form, programs=programs)



@main.route('/clients', methods=['GET', 'POST'])
def clients():
    form = ClientForm()
    if form.validate_on_submit():
        client = Client(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone=form.phone.data,
            address=form.address.data,
            date_of_birth=form.date_of_birth.data,
            gender=form.gender.data
        )
        db.session.add(client)
        db.session.commit()
        flash('Client added successfully!', 'success')
        return redirect(url_for('main.clients'))
    
    # Order by last name then first name
    clients = Client.query.order_by(Client.last_name, Client.first_name).all()
    return render_template('clients.html', 
                         form=form, 
                         clients=clients,
                         search_query=None)




@main.route('/client/<int:client_id>', methods=['GET', 'POST'])
def client_detail(client_id):
    client = Client.query.get_or_404(client_id)
    form = EnrollmentForm()
    form.programs.choices = [(p.id, p.name) for p in Program.query.order_by('name')]
    
    if form.validate_on_submit():
        for program_id in form.programs.data:
            program = Program.query.get(program_id)
            if program and program not in client.programs:
                client.programs.append(program)
        db.session.commit()
        flash('Client enrolled in programs!', 'success')
        return redirect(url_for('main.client_detail', client_id=client.id))
    
    return render_template('client_detail.html', client=client, form=form)




@main.route('/client/<int:client_id>/remove_program/<int:program_id>')
def remove_enrollment(client_id, program_id):
    client = Client.query.get_or_404(client_id)
    program = Program.query.get_or_404(program_id)
    
    if program in client.programs:
        client.programs.remove(program)
        db.session.commit()
        flash('Program removed from client!', 'success')
    
    return redirect(url_for('main.client_detail', client_id=client.id))




@main.route('/clients/search')
def search_clients():
    search_query = request.args.get('q', '').strip()
    
    if not search_query:
        return redirect(url_for('main.clients'))
    
    clients = Client.query.filter(
        (Client.first_name.ilike(f'%{search_query}%')) |
        (Client.last_name.ilike(f'%{search_query}%')) |
        (Client.email.ilike(f'%{search_query}%')) |
        (Client.phone.ilike(f'%{search_query}%'))
    ).all()
    
    return render_template('search_results.html', 
                        clients=clients,
                        search_query=search_query)




@main.route('/client/<int:client_id>/edit', methods=['GET', 'POST'])
def edit_client(client_id):
    client = Client.query.get_or_404(client_id)
    form = ClientForm(obj=client)
    
    if form.validate_on_submit():
        form.populate_obj(client)
        db.session.commit()
        flash('Client updated successfully!', 'success')
        return redirect(url_for('main.client_detail', client_id=client.id))
    
    return render_template('edit_client.html', form=form, client=client)




@main.route('/client/<int:client_id>/delete', methods=['POST'])
def delete_client(client_id):
    client = Client.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    flash('Client deleted successfully!', 'success')
    return redirect(url_for('main.clients'))



@main.route('/client/<int:client_id>/enroll', methods=['GET', 'POST'])
def enroll_client(client_id):
    client = Client.query.get_or_404(client_id)
    form = EnrollmentForm()  # Create form instance
    
    # Get all available programs
    all_programs = Program.query.order_by(Program.name).all()
    
    if request.method == 'POST':
        try:
            # Get selected program IDs
            selected_programs = request.form.getlist('programs')
            
            # Clear existing enrollments
            Enrollment.query.filter_by(client_id=client.id).delete()
            
            # Add new enrollments
            for program_id in selected_programs:
                enrollment = Enrollment(
                    client_id=client.id,
                    program_id=program_id,
                    enrollment_date=datetime.utcnow(),
                    is_active=True
                )
                db.session.add(enrollment)
            
            db.session.commit()
            flash('Enrollment updated successfully!', 'success')
            return redirect(url_for('main.client_detail', client_id=client.id))
        
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating enrollment: {str(e)}', 'danger')
    
    return render_template('enroll_client.html',
                         client=client,
                         all_programs=all_programs,
                         form=form)  # Pass the form to template