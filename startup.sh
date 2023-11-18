cd OHare/RasiMedicalApp/microservices/supply
sudo apt update
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8080




cd OHare/RasiMedicalApp/microservices/formula
sudo apt update
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8080

