from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ContactForm,ProductForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Category

from django.db.models import Q

class ProductListView(ListView):
    model = Product
    template_name = 'crafts/products.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        qs = Product.objects.all().order_by('-created_at')

        q = self.request.GET.get('q')
        cat = self.request.GET.get('category')

        if q:
            qs = qs.filter(
                Q(title__icontains=q) |
                Q(description__icontains=q)
            )

        if cat:
            qs = qs.filter(category__slug=cat)

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = Category.objects.all()          # for sidebar / dropdown
        ctx['selected_category'] = self.request.GET.get('category')  # highlight filter
        ctx['query'] = self.request.GET.get('q', '')        # keep search in box
        return ctx

class ProductDetailView(DetailView):
    model = Product
    template_name = 'crafts/product_detail.html'
    context_object_name = 'product'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = Category.objects.all()
        return ctx

class IndexView(ListView):
    model = Product
    template_name = "crafts/index.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = Category.objects.all()
        return ctx


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'admin/product_form.html'
    success_url = reverse_lazy('crafts:products')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'admin/product_form.html'
    success_url = reverse_lazy('crafts:products')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'admin/product_confirm_delete.html'
    success_url = reverse_lazy('crafts:products')



def index(request):
    latest = Product.objects.all()[:6]
    return render(request, 'crafts/index.html', {'products': latest})
    

def products(request):
    items = Product.objects.all()
    return render(request, 'crafts/products.html', {'products': items})

def product_detail(request, slug):
    item = get_object_or_404(Product, slug=slug)
    return render(request, 'crafts/product_detail.html', {'product': item})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks! Your message was sent.')
            return redirect('crafts:contact')
    else:
        form = ContactForm()
    return render(request, 'crafts/contact.html', {'form': form})



def admin_products(request):
    products = Product.objects.all()
    product_count = products.count()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('crafts:admin_products')
    else:
        form = ProductForm()

    return render(request, 'crafts/admin_products.html', {
        'products': products,
        'product_count': product_count,
        'form': form
    })



def admin_dashboard_view(request):
    context = {
        'total_products': Product.objects.count(),
        'total_categories': Category.objects.count(),
        'total_messages': ContactMessage.objects.count(),
    }
    return render(request, "admin/custom_index.html", context)


from django.contrib.auth.decorators import login_required


