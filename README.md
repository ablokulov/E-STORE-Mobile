# 🛒 Cyber Store – E-Commerce Backend API

## 🎯 Maqsad

Ushbu loyiha zamonaviy **e-commerce platforma** uchun yozilgan professional **backend REST API** hisoblanadi.

### Asosiy maqsadlar:

- REST API dizayn (**best practices**)
- Authentication & Authorization (**JWT**)
- Business Logic & Validation
- Performance (**ORM optimizatsiya**)
- To‘liq e-commerce flow (**Cart → Order → Payment**)
- Swagger / Redoc bilan hujjatlashtirish

---

## 1️⃣ Texnologiyalar (Majburiy)

- **Python 3.12+**
- **Django**
- **Django REST Framework (DRF)**
- **JWT Authentication**  
  (`djangorestframework-simplejwt`)
- **PostgreSQL**
- **Redis** (Cart / Cache)
- **Swagger / Redoc**  
  (`drf-spectacular`)
- **.env** (environment variables)
- **Git + GitHub** (public repository)

---


## 2️⃣ Foydalanuvchi Rollari (RBAC)

| Role  | Tavsif |
|------|-------|
| **ADMIN** | Tizimni to‘liq boshqaradi (users, products, orders) |
| **STAFF** | Operator / manager (product va orderlar bilan ishlaydi) |
| **USER** | Oddiy foydalanuvchi (sotib olish, buyurtma) |
| **GUEST** | Login qilmagan foydalanuvchi (faqat ko‘rish) |

📌 **Eslatma:**  
Operator, kontent menejer, support — barchasi backend’da **STAFF** hisoblanadi.

---

## 3️⃣ Ma’lumotlar Modellari

### 👤 User (Custom User)

| Field | Type / Description |
|------|-------------------|
| `id` | UUID / Integer |
| `email` | Email (unique) |
| `username` | Username |
| `role` | USER / STAFF / ADMIN |
| `is_active` | Boolean |
| `is_staff` | Boolean |
| `is_superuser` | Boolean |
| `created_at` | DateTime |

---

### 👤 Profile

| Field | Type / Description |
|------|-------------------|
| `id` | UUID / Integer |
| `user` | OneToOne → User |
| `first_name` | String |
| `last_name` | String |
| `phone` | String |

---

### 🏠 Address

| Field | Type / Description |
|------|-------------------|
| `id` | UUID / Integer |
| `user` | ForeignKey → User |
| `city` | String |
| `street` | String |
| `postal_code` | String |
| `is_default` | Boolean |


### 📦 Category

| Field | Type / Description |
|------|-------------------|
| `id` | UUID / Integer |
| `name` | String |
| `slug` | Slug (unique) |
| `created_at` | DateTime |

---

### 📱 Product

| Field | Type / Description |
|------|-------------------|
| `id` | UUID / Integer |
| `category` | ForeignKey → Category |
| `name` | String |
| `brand` | String |
| `price` | Decimal |
| `discount_price` | Decimal (nullable) |
| `description` | Text |
| `stock` | Integer |
| `rating` | Float |
| `created_at` | DateTime |

---

### 🖼 ProductImage

| Field | Type / Description |
|------|-------------------|
| `id` | UUID / Integer |
| `product` | ForeignKey → Product |
| `image` | ImageField |

---

### ❤️ Wishlist

| Field | Type / Description |
|------|-------------------|
| `id` | UUID / Integer |
| `user` | ForeignKey → User |
| `product` | ForeignKey → Product |
| `created_at` | DateTime |

📌 **Eslatma:**  
`user + product` kombinatsiyasi **unique** bo‘lishi kerak.

---

### 🛒 Cart

| Field | Type / Description |
|------|-------------------|
| `id` | UUID / Integer |
| `user` | OneToOne → User |
| `updated_at` | DateTime |

📌 **Eslatma:**  
Cart ma’lumotlari **Redis** orqali cache qilinadi.

---

### 🛍 CartItem

| Field | Type / Description |
|------|-------------------|
| `id` | UUID / Integer |
| `cart` | ForeignKey → Cart |
| `product` | ForeignKey → Product |
| `quantity` | Integer |

📌 **Eslatma:**  
`cart + product` kombinatsiyasi **unique** bo‘lishi kerak.

---

### 📦 Order

| Field | Type / Description |
|------|-------------------|
| `id` | UUID / Integer |
| `user` | ForeignKey → User |
| `total_price` | Decimal |
| `status` | pending / paid / cancelled / shipped |
| `created_at` | DateTime |

---

### 📦 OrderItem

| Field | Type / Description |
|------|-------------------|
| `id` | UUID / Integer |
| `order` | ForeignKey → Order |
| `product` | ForeignKey → Product |
| `price` | Decimal |
| `quantity` | Integer |

---

### 💳 Payment

| Field | Type / Description |
|------|-------------------|
| `id` | UUID / Integer |
| `order` | ForeignKey → Order |
| `payment_method` | String |
| `payment_status` | pending / success / failed |
| `transaction_id` | String |
| `created_at` | DateTime |

## ⭐ Review

| Field | Type / Description |
|------|-------------------|
| `id` | UUID / Integer |
| `user` | ForeignKey → User |
| `product` | ForeignKey → Product |
| `rating` | Integer (1–5) |
| `comment` | Text |
| `created_at` | DateTime |

📌 **Eslatma:**  
- Review faqat mahsulotni **sotib olgan foydalanuvchi** tomonidan yozilishi mumkin  
- `user + product` kombinatsiyasi **unique** bo‘lishi mumkin (ixtiyoriy)

---

## 4️⃣ Funksional Talablar

### 🔐 Authentication & Authorization

- User register
- Login
- JWT access & refresh token
- Role-based permissions (RBAC)
- Protected endpoints

---

### 🛒 USER imkoniyatlari

- Mahsulotlarni ko‘rish
- Filter & search
- Savatchaga qo‘shish
- Wishlist (❤️)
- Buyurtma berish
- To‘lov qilish (mock / stripe-ready)
- Review va rating yozish

❌ **Cheklov:**  
- Boshqa foydalanuvchilarning buyurtmalariga kira olmaydi

---

### 🛡 STAFF imkoniyatlari (Operator)

- Product create / update
- Order status o‘zgartirish
- Review moderatsiya
- Buyurtmalarni ko‘rish

---

### 🛡 ADMIN imkoniyatlari

- Category CRUD
- Product CRUD
- Order management
- Payment monitoring
- User & role management

---

## 5️⃣ Business Logic (Eng Muhim Qism)

### ✅ Validation Rules

- ❌ Product `stock = 0` bo‘lsa buyurtma qilinmaydi
- ❌ Cart’da bitta product takror qo‘shilmaydi
- ✅ Order yaratilganda product `stock` kamayadi
- ❌ Review faqat order egasi tomonidan yoziladi
- ❌ Rating faqat **1–5** oralig‘ida bo‘lishi kerak
- ✅ Payment `paid` bo‘lsa order status `paid` ga o‘zgaradi

---

## 6️⃣ Permission Talablari

### Custom Permission’lar

- `IsAdmin`
- `IsStaff`
- `IsAuthenticated`
- `IsOwner`

### 📌 Misollar

- **USER** → faqat o‘z cart / order / review
- **STAFF** → product va order management
- **ADMIN** → tizim bo‘yicha to‘liq ruxsat

## 7️⃣ API Endpoints (Minimum Requirement)

### 🔐 Authentication

| Method | Endpoint | Description |
|------|---------|-------------|
| POST | `/api/auth/register/` | User registration |
| POST | `/api/auth/login/` | User login |
| POST | `/api/auth/token/refresh/` | JWT refresh token |

---

### 📦 Categories & Products

| Method | Endpoint | Description |
|------|---------|-------------|
| GET | `/api/categories/` | Category list |
| GET | `/api/products/` | Product list |
| GET | `/api/products/{id}/` | Product detail |

---

### 🛒 Cart

| Method | Endpoint | Description |
|------|---------|-------------|
| POST | `/api/cart/items/` | Add product to cart |
| GET | `/api/cart/` | Get user cart |
| DELETE | `/api/cart/items/{id}/` | Remove cart item |

---

### 📦 Orders

| Method | Endpoint | Description |
|------|---------|-------------|
| POST | `/api/orders/` | Create order |
| GET | `/api/orders/me/` | User orders |

---

### 💳 Payments

| Method | Endpoint | Description |
|------|---------|-------------|
| POST | `/api/payments/` | Create payment |

---

## 8️⃣ Qo‘shimcha Talablar (Plus)

### 📄 Pagination
- Global pagination (DRF)
- Page size configurable

### 🔍 Filtering
- `category`
- `price`
- `brand`

### 🔎 Search
- Product name bo‘yicha qidiruv

### ⚙️ Performance & Code Quality
- Serializer-level validation
- `select_related` / `prefetch_related`
- Clean & modular architecture
- Service layer (business logic ajratish)

---

## 9️⃣ Swagger & README (Majburiy)

### 📘 Swagger / Redoc

- Barcha endpointlar hujjatlashtirilgan
- Request / Response example’lar mavjud

| Tool | URL |
|----|----|
| Swagger UI | `/api/swagger/` |
| Redoc | `/api/redoc/` |

---

## 📁 Project Structure
```
E-STORE-Mobile/
├── apps/
│   ├── accounts/
│   ├── products/
│   ├── categories/
│   ├── cart/
│   ├── orders/
│   ├── payments/
│   ├── reviews/
├── config/
│   ├── settings/
│   ├── urls.py
│   └── asgi.py
├── .env.example
├── requirements/
├── manage.py
├── README.md
```

## 🚀 PROJECT SETUP

git clone https://github.com/ablokulov/E-STORE-Mobile.git
cd cyber-store-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements/local.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver



## 👨‍💻 Author

**Nodirbek Abloqulov**  
Backend Developer  
Python / Django / Django REST Framework (DRF)
