@echo off

set dpi=200

if not "%1"=="" (
	set dpi=%1
)

python manage.py graph_models -a > database.dot
dot -Tpng -Gdpi=%dpi% database.dot > database.png