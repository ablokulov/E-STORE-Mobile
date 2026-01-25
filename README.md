# 🛒 PROJECT

## **Cyber Store – E-Commerce Backend API**

### 🎯 Maqsad:
* REST API dizayn
* Authentication & Authorization (JWT, Permission)
* Business Logic & Validation
* Performance (ORM optimizatsiya)
* E-Commerce flow (Cart, Order, Payment)
* API hujjatlashtirish

---

## 1️⃣ TEXNOLOGIYALAR (MAJBURIY)

* Python 3.x
* Django
* Django Rest Framework (DRF)
* JWT Authentication (`djangorestframework-simplejwt`)
* PostgreSQL
* Swagger / Redoc (`drf-spectacular`)
* `.env` (environment variables)
* Git + GitHub (public repository)

---

## 2️⃣ FOYDALANUVCHI ROLLARI

| Role      | Tavsif                                      |
| --------- | ------------------------------------------- |
| **Admin** | Tizim va mahsulotlarni boshqaradi           |
| **User**  | Mahsulot sotib oladi, buyurtma beradi       |

---

## 3️⃣ MA’LUMOTLAR MODELLARI

### 👤 User (Custom User)

```text
id
username
email
password
is_active
created_at
```
### 📦 Category
```text
id
name
slug
created_at
```
### 📱 Product
```
id
category (FK)
name
brand
price
discount_price
description
stock
rating
created_at
```
### 🖼 ProductImage
```
id
product (FK)
image
```
### ❤️ Wishlist
```
id
user (FK)
product (FK)
created_at
```
### 🛒 Cart
```
id
user (OneToOne)
updated_at
```
### 🛍 CartItem
```
id
cart (FK)
product (FK)
quantity

```
### 📦 Order
```
id
user (FK)
total_price
status (pending / paid / cancelled)
created_at

```
### 📦 OrderItem

```
id
order (FK)
product (FK)
price
quantity

```
### 💳 Payment

```
id
order (FK)
payment_method
payment_status
transaction_id
created_at

```
### ⭐ Review
```
id
user (FK)
product (FK)
rating (1–5)
comment
created_at

```
## 4️⃣ FUNKSIONAL TALABLAR

### 🔐 Authentication & Authorization

- User register  
- Login  
- JWT access & refresh token  
- Protected endpoints  

---

### 🛒 User imkoniyatlari

- Mahsulotlarni ko‘rish  
- Filter & search  
- Savatchaga qo‘shish  
- Wishlist qo‘shish  
- Buyurtma berish  
- To‘lov qilish (mock / stripe-ready)  
- Review va rating yozish  

❌ Boshqa user buyurtmalariga kira olmaydi

---

### 🛡 Admin imkoniyatlari

- Category CRUD  
- Product CRUD  
- Order management  
- Payment monitoring  
- User management  

---

## 5️⃣ BUSINESS LOGIC (ASOSIY BAHOLANADIGAN QISM)

### ✅ Validation Rules

- ❌ Stock `0` bo‘lsa product buyurtma qilinmaydi  
- ❌ Cart’da bir product takror qo‘shilmaydi  
- ✅ Order yaratilganda product stock kamayadi  
- ❌ Faqat order egasi review yozadi  
- ❌ Rating `1–5` oralig‘ida bo‘lishi shart  
- ✅ Payment `paid` bo‘lsa order status `paid`  

---

## 6️⃣ PERMISSION TALABLARI

Custom permission’lar:

- `IsAdmin`
- `IsAuthenticated`
- `IsOwner`

📌 Misollar:

- User → faqat **o‘z cart / order**
- Admin → **hammasi**

---

## 7️⃣ API ENDPOINTLAR (MINIMUM REQUIREMENT)

```http
POST   /auth/register/
POST   /auth/login/
POST   /auth/token/refresh/

GET    /categories/
GET    /products/
GET    /products/{id}/

POST   /cart/items/
GET    /cart/
DELETE /cart/items/{id}/

POST   /orders/
GET    /orders/me/

POST   /payments/
```

## 8️⃣ QO‘SHIMCHA TALABLAR (PLUS BALL)

- Pagination  
- Filtering:
  - category
  - price
  - brand  
- Search:
  - product name  
- Serializer validation  
- `select_related` / `prefetch_related`  
- Clean architecture  

---

## 9️⃣ SWAGGER & README (MAJBURIY)

### Swagger

- Barcha endpointlar hujjatlashtirilgan  
- Request / Response example’lar  

### README ichida

- Project setup  
- `.env.example`  
- Migration & superuser  
- API’dan foydalanish  

---

## 📁 PROJECT STRUCTURE
```

cyber_store_api/
├── apps/
│   ├── users/
│   ├── products/
│   ├── cart/
│   ├── orders/
│   ├── payments/
│   ├── reviews/
├── core/
│   ├── settings.py
│   ├── urls.py
├── .env.example
├── requirements.txt
├── README.md
```


## 📌 ALL ENDPOINTS (FULL LIST)

### Base URL

```text
/api
### Authentication

```http
Authorization: Bearer <access_token>
```

## 🛒 PRODUCTS

| Method | Endpoint            | Description      | Access |
|------|---------------------|------------------|--------|
| GET  | `/products/`        | Products list    | Public |
| GET  | `/products/{id}/`   | Product detail   | Public |
| POST | `/products/`        | Create product   | Admin  |
| PATCH| `/products/{id}/`   | Update product   | Admin  |
| DELETE | `/products/{id}/` | Delete product   | Admin  |

---

## 🛒 CART

| Method | Endpoint                | Description      | Access |
|------|-------------------------|------------------|--------|
| GET  | `/cart/`                | My cart          | User   |
| POST | `/cart/items/`          | Add to cart      | User   |
| DELETE | `/cart/items/{id}/`   | Remove from cart | User   |

---

## 📦 ORDERS

| Method | Endpoint      | Description  | Access |
|------|---------------|--------------|--------|
| POST | `/orders/`    | Create order | User   |
| GET  | `/orders/me/` | My orders    | User   |
| GET  | `/orders/`    | All orders   | Admin  |

---

## ⭐ REVIEWS

| Method | Endpoint                  | Description       | Access |
|------|---------------------------|-------------------|--------|
| POST | `/products/{id}/reviews/` | Add review        | User   |
| GET  | `/products/{id}/reviews/` | Product reviews  | Public |

---

## 👨‍💻 Author

**Nodirbek Abloqulov**  
Backend Developer (Python / Django / DRF)








