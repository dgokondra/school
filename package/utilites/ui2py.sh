# pyrcc5 ../resources/images.qrc -o ../view/images_rc.py
# Пример генерации python скрипта из исходника в QtDesigner
# python -m PyQt5.uic.pyuic -x ../resources/ui/имя_исходника.ui -o ../views/имя_скрипта.py

pyrcc5 ../resources/images.qrc -o ../view/images_rc.py
pyuic5 -x ../resources/ui/authorization.ui -o ../views/authorization_view.py
pyuic5 -x ../resources/ui/start.ui -o ../views/start_view.py
pyuic5 -x ../resources/ui/select_object.ui -o ../views/select_object_view.py
pyuic5 -x ../resources/ui/add_schoolbook.ui -o ../views/add_schoolbook_view.py
pyuic5 -x ../resources/ui/add_fictionbook.ui -o ../views/add_fictionbook_view.py
pyuic5 -x ../resources/ui/search_schoolbook.ui -o ../views/search_schoolbook_view.py
pyuic5 -x ../resources/ui/search_fictionbook.ui -o ../views/search_fictionbook_view.py
pyuic5 -x ../resources/ui/schoolbook_card.ui -o ../views/schoolbook_card_view.py
pyuic5 -x ../resources/ui/fictionbook_card.ui -o ../views/fictionbook_card_view.py
pyuic5 -x ../resources/ui/search_results.ui -o ../views/search_results_view.py
pyuic5 -x ../../tests/unit/fixtures/widget_for_utils_testing.ui -o ../../tests/unit/fixtures/widget_test.py
