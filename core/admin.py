from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.contrib import messages
from django import forms
from .models import Pedido, Producto


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        productos = cleaned_data.get('productos', [])
        cliente = cleaned_data.get('cliente')

        if not productos or not cliente:
            return cleaned_data  # Deja que otros validadores se encarguen

        total = sum(p.precio for p in productos)
        self._total_calculado = total  # Guardamos el total para usarlo en save()

        if cliente.saldo < total:
            raise ValidationError(
                f"Saldo insuficiente. El cliente tiene ${cliente.saldo:.2f} y el pedido cuesta ${total:.2f}."
            )

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.total = getattr(self, '_total_calculado', 0)

        if commit:
            instance.save()
            self.save_m2m()
            cliente = instance.cliente
            cliente.saldo -= instance.total
            cliente.save()

            if self.request:
                messages.success(
                    self.request,
                    f"Pedido creado. Se descontaron ${instance.total:.2f} del saldo del cliente."
                )

        return instance


class PedidoAdmin(admin.ModelAdmin):
    form = PedidoForm
    exclude = ('total',)
    filter_horizontal = ('productos',)

    def get_form(self, request, obj=None, **kwargs):
        form_class = super().get_form(request, obj, **kwargs)

        class FormWithRequest(form_class):
            def __new__(cls, *args, **kw):
                kw['request'] = request
                return form_class(*args, **kw)

        return FormWithRequest

    def save_related(self, request, form, formsets, change):
        # Ya no es necesario calcular ni validar aquí
        super().save_related(request, form, formsets, change)


admin.site.register(Pedido, PedidoAdmin)
