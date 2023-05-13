var swiper = new Swiper(".slide-content", {
    slidesPerView: 3,
    spaceBetween: 25,
    loop: true,
    centerSlide: 'true',
    fade: 'true',
    grabCursor: 'true',
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
      dynamicBullets: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },

    breakpoints:{
        0: {
            slidesPerView: 1,
        },
        520: {
            slidesPerView: 2,
        },
        950: {
            slidesPerView: 3,
        },
    },
});

fetch('http://127.0.0.1:8000/api/content/')
.then(response => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('API request failed');
    }
})
.then(data => {
    // Process the response data and populate the home page
    console.log(data);
    console.log("aaaaaaaaaaa")
    // Do something with the fetched contents
})
.catch(error => {
    // Handle any errors that occurred during the API request
    console.error(error);
});
