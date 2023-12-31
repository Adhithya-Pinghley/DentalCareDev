# Generated by Django 4.2.2 on 2023-09-14 07:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('contactNumber', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('specialization', models.CharField(max_length=100)),
                ('passwordHash', models.CharField(max_length=64)),
                ('emailHash', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'healthcentre_doctor',
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MedicineName', models.CharField(max_length=200)),
                ('beforeAfter', models.CharField(max_length=200)),
                ('Morning', models.CharField(max_length=200)),
                ('Afternoon', models.CharField(max_length=200)),
                ('Night', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'healthcentre_medicine',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('contactNumber', models.CharField(db_column='contactnumber', max_length=10)),
                ('email', models.EmailField(max_length=255)),
                ('rollNumber', models.CharField(db_column='rollnumber', max_length=8)),
                ('passwordHash', models.CharField(db_column='passwordhash', max_length=64)),
                ('emailHash', models.CharField(db_column='emailhash', max_length=64)),
            ],
            options={
                'db_table': 'healthcentre_patient',
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescriptionText', models.CharField(db_column='prescriptiontext', default='', max_length=2000)),
                ('prescribingDoctor', models.CharField(db_column='prescribingdoctor', default='', max_length=2000)),
                ('prescribingPatient', models.CharField(db_column='prescribingpatient', default='', max_length=2000)),
                ('NoOfDays', models.CharField(db_column='noofdays', max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('isNew', models.BooleanField(db_column='isnew', default=True)),
                ('isCompleted', models.BooleanField(db_column='iscompleted', default=False)),
                ('symptoms', models.CharField(max_length=2000)),
                ('doctor', models.ForeignKey(db_column='doctor_id', on_delete=django.db.models.deletion.CASCADE, related_name='doctorRecords', to='HealthCentre.doctor')),
                ('medicine', models.ManyToManyField(to='HealthCentre.medicine')),
                ('patient', models.ForeignKey(db_column='patient_id', on_delete=django.db.models.deletion.CASCADE, related_name='patientRecords', to='HealthCentre.patient')),
            ],
            options={
                'db_table': 'healthcentre_prescription',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('subject', models.CharField(max_length=2000)),
                ('notes', models.TextField()),
                ('appointmentpatient', models.CharField(default='', max_length=2000)),
                ('appointmentdoctor', models.CharField(default='', max_length=2000)),
                ('AppointmentTimeStamp', models.DateTimeField(auto_now_add=True, db_column='appointmenttimestamp')),
                ('doctorPres', models.ForeignKey(db_column='doctorpres', on_delete=django.db.models.deletion.CASCADE, related_name='doctorPrescRecords', to='HealthCentre.doctor')),
                ('patientPres', models.ForeignKey(db_column='patientpres', on_delete=django.db.models.deletion.CASCADE, related_name='patientPrescRecords', to='HealthCentre.patient')),
            ],
            options={
                'db_table': 'healthcentre_appointment',
            },
        ),
    ]
