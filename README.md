Deployed project: https://desla-d87b87e86338.herokuapp.com/

# Desla Art & Tattoo E-commerce

An e-commerce web application designed for **Desla**, a professional artist and tattoo studio. This platform allows users to browse and purchase original artwork, book tattoo sessions, and explore a gallery of finished pieces. Built using **Django**, **PostgreSQL**, **Stripe**, and **AWS S3**, it offers a seamless and secure shopping and booking experience.

## 🖌️ About the Project

**Desla Art & Tattoo** is an online platform that connects customers with Desla's unique artwork and professional tattoo services.  
The main goal of the project is to create a clean, intuitive, and efficient experience for art collectors and tattoo enthusiasts, offering:

- A responsive storefront
- Secure checkout system
- Appointment booking functionality
- Full content management for products and gallery

---

## 🚀 Features

- User Registration & Authentication
- Artwork Browsing and Categorization
- Tattoo Session Booking System
- Shopping Cart and Checkout (powered by Stripe)
- User Profiles with Order History
- Admin Dashboard for Content Management
- Responsive Design for Mobile, Tablet, and Desktop
- Email Notifications for Orders and Bookings
- Cloud Storage for Images (AWS S3)
- SEO and Performance Optimization

---

## 🛠️ Technologies Used

- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
- **Backend:** Django, Python
- **Database:** PostgreSQL
- **Payments:** Stripe API
- **Storage:** AWS S3 (Static and Media Files)
- **Deployment:** Heroku
- **Other Tools:** Git, GitHub, Django Crispy Forms, Cloudinary (optional)

---

## 💻 Installation and Setup

To run this project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/desla-ecommerce.git
   cd desla-ecommerce
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - `SECRET_KEY`
   - `STRIPE_PUBLIC_KEY`
   - `STRIPE_SECRET_KEY`
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `DATABASE_URL`

5. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser for the admin panel:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

---

## 📖 Usage

- Browse artwork and add items to the shopping cart.
- Register or login to proceed to checkout.
- Use the booking system to request tattoo appointments.
- Manage your account, view past orders, and update personal information.

---

## ☁️ Deployment

The live project is deployed on **Heroku**, with static and media files served from **AWS S3**.

To deploy:

- Push code to GitHub.
- Connect GitHub repo to Heroku.
- Set config vars on Heroku for environment variables.
- Set up AWS S3 bucket for static/media files.

---

## 🙌 Credits

- Developed and designed by **Felipe Nast Loyola**.
- Tattoo and artwork by **Desla**.
- Frameworks and libraries: Django, Bootstrap, Stripe, AWS, PostgreSQL.
