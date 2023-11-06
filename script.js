document.addEventListener("DOMContentLoaded", function () {
    const addToCartButtons = document.querySelectorAll(".add-to-cart");
    const cartItems = document.querySelector(".cart-items");
    const cartTotal = document.getElementById("cart-total");

    let total = 0;

    addToCartButtons.forEach((button) => {
        button.addEventListener("click", () => {
            const productCard = button.closest(".product-card");
            const productName = productCard.querySelector("h2").textContent;
            const productPrice = parseFloat(productCard.querySelector("p:last-child").textContent.replace("$", ""));
            total += productPrice;

            const cartItem = document.createElement("li");
            cartItem.textContent = `${productName} - $${productPrice}`;
            cartItems.appendChild(cartItem);

            cartTotal.textContent = total.toFixed(2);
        });
    });
});


function mobiles() { 
    let input = document.getElementById('searchbar').value 
    input=input.toLowerCase(); 
    let x = document.getElementsByClassName('mobiles'); 
      
    for (i = 0; i < x.length; i++) {  
        if (!x[i].innerHTML.toLowerCase().includes(input)) { 
            x[i].style.display="none"; 
        } 
        else { 
            x[i].style.display="list-item";                  
        } 
    } 
}
p = document.getElementById("price");
p.addEventListener("click",() => {
    pp = document.getElementById("frame");
    pp.src = "https://pricehistoryapp.com/embed/iphone-14-pro-max-1tb-deep-purple"
    
})