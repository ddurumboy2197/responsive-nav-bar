# Bu kod fragmenti Tailwind CSS bilan ishlaydi, lekin Python dasturlash tili uchun mo'ljallangan emas.
# Agar siz Tailwind CSS bilan ishlashingiz kerak bo'lsa, unda siz HTML, CSS va JavaScript kodi yozishingiz kerak.
# Python dasturlash tili uchun mo'ljallangan kod fragmenti quyidagicha bo'ladi:
# import tkinter as tk

# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")

#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                              command=self.master.destroy)
#         self.quit.pack(side="bottom")

#     def say_hi(self):
#         print("hi there, everyone!")

# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()
```

Agar siz Tailwind CSS bilan ishlashingiz kerak bo'lsa, quyidagicha kod fragmenti yozishingiz kerak:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Navigation Bar</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body>
    <nav class="bg-gray-800 text-white p-4 flex justify-between items-center">
        <a href="#" class="text-2xl font-bold">Logo</a>
        <button class="md:hidden block" id="mobile-menu-button">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
        </button>
        <div class="hidden md:flex md:items-center md:space-x-4">
            <a href="#" class="text-gray-300 hover:text-white transition duration-300 ease-in-out">Home</a>
            <a href="#" class="text-gray-300 hover:text-white transition duration-300 ease-in-out">About</a>
            <a href="#" class="text-gray-300 hover:text-white transition duration-300 ease-in-out">Contact</a>
        </div>
    </nav>
    <div class="hidden md:hidden md:flex md:items-center md:space-x-4" id="mobile-menu">
        <a href="#" class="text-gray-300 hover:text-white transition duration-300 ease-in-out">Home</a>
        <a href="#" class="text-gray-300 hover:text-white transition duration-300 ease-in-out">About</a>
        <a href="#" class="text-gray-300 hover:text-white transition duration-300 ease-in-out">Contact</a>
    </div>

    <script>
        const mobileMenuButton = document.getElementById('mobile-menu-button');
        const mobileMenu = document.getElementById('mobile-menu');

        mobileMenuButton.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    </script>
</body>
</html>
