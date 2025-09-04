from .models import Employee
import django_filters

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name = "designation", lookup_expr = 'iexact')
    emp_name = django_filters.CharFilter(field_name="emp_name", lookup_expr ='icontains')

    # id = django_filters.RangeFilter(field_name='id')

    
    # char baset range filtering
    id_min = django_filters.CharFilter(method='filter_by_id_range',label='From Emp id')
    id_max = django_filters.CharFilter(method='filter_by_id_range',label ='To Emp id')


    class Meta:
        model = Employee
        fields =['designation','emp_name','id_min','id_max']


    def filter_by_id_range(self, queryset, name, value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte=value)
        elif name == 'id_max':
            return queryset.filter(emp_id__lte=value)
        return queryset