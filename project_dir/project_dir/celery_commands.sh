echo "Celery WORKER RUN >>>>>>>>> Created By IVAN GONCHAROV !"

celery -A project_dir worker -l INFO

echo "Celery BEAT RUN >>>>>>>>> Created By IVAN GONCHAROV !"

celery -A project_dir beat -l INFO