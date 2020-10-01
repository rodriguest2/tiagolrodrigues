from webpage.models import Category

cat_choices = Category.objects.all().values_list('name','name')
cat_list = []

for item in cat_choices:
    cat_list.append(item)
