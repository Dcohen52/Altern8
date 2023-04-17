// // Get a reference to the navigation buttons
// const navButtons = document.querySelectorAll('#top-bar input[type="button"]');

// // Get a reference to the content divs
// const contentDivs = document.querySelectorAll('.content');

// // Add click event listeners to the navigation buttons
// navButtons.forEach(button => {
//     button.addEventListener('click', () => {
//         // Get the ID of the content div to show
//         const target = button.id.replace('-button', '-page');

//         // Hide all content divs
//         contentDivs.forEach(div => {
//             if (div.id === target) {
//                 div.classList.add('active');
//             } else {
//                 if (div.classList.contains('active')) {
//                     div.classList.remove('active');
//                 }
//             }
//         });

//         // Set a timeout to add the "visible" class after the content is hidden
//         setTimeout(() => {
//             contentDivs.forEach(div => {
//                 if (div.id === target) {
//                     div.classList.add('visible');
//                 } else {
//                     if (div.classList.contains('visible')) {
//                         div.classList.remove('visible');
//                     }
//                 }
//             });
//         }, 10000);
//     });
// });
