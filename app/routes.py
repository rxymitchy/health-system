from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Program, Client, db
from app.forms import ProgramForm, ClientForm, EnrollmentForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return redirect(url_for('main.programs'))

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
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data
        )
        db.session.add(client)
        db.session.commit()
        flash('Client added successfully!', 'success')
        return redirect(url_for('main.clients'))
    
    clients = Client.query.order_by(Client.name).all()
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
    
    # Search in name, email, or phone fields
    clients = Client.query.filter(
        (Client.name.ilike(f'%{search_query}%')) |
        (Client.email.ilike(f'%{search_query}%')) |
        (Client.phone.ilike(f'%{search_query}%'))
    ).all()
    
    return render_template('clients.html', 
                         clients=clients, 
                         search_query=search_query,
                         form=ClientForm())