function nav(){
    // let listContainer=document.createElement("div")
    let navbar=document.getElementById("navbar") 
    let navIcon=document.getElementById("nav-icon")
    let list=document.getElementById('list')
    list.classList.toggle('active');
    
}
// var result = [];
// let left=0
// let right=2
fetch('https://testimonialapi.toolcarton.com/api').then(function(res){
    return res.json()
}).then(data=>{
    // console.log(data)
    // console.log(typeof(data))
    // let json_data=data
    let testimonials=document.getElementById('testimonials__slides')
    let eachCardWidth = testimonials.offsetWidth / 3;
    // console.log("eachCardWidth",eachCardWidth);
    for(var i in data)
    {    
    // {   result.push([i, data[i]]);    
            
            let testimonial_div=document.createElement('div')
            let testimonial_img=document.createElement('div')
            let img=document.createElement('img')
            img.setAttribute('class','avatar')
            img.src=`${data[i].avatar}`
            testimonial_img.appendChild(img)
            let testimonial_name=document.createElement('h6')
            testimonial_name.innerHTML=`${data[i].name}`
            let testimonial_position=document.createElement('p')
            testimonial_position.innerHTML=`${data[i].designation}`
            let testimonial_desc=document.createElement('p')
            testimonial_desc.innerHTML=`${data[i].message}`
            testimonial_div.setAttribute('class','testimonial_items')
            testimonial_div.setAttribute('id',`cl${i}`)
            // testimonial_div.style.width = `${eachCardWidth}vw`
            testimonial_img.setAttribute('class','test_img')
            testimonial_name.setAttribute('class','test_name')
            testimonial_position.setAttribute('class','test_position')
            testimonial_desc.setAttribute('class','test_desc')
            testimonial_div.appendChild(testimonial_img)
            testimonial_div.appendChild(testimonial_name)
            testimonial_div.appendChild(testimonial_position)
            testimonial_div.appendChild(testimonial_desc)
            testimonials.appendChild(testimonial_div)
            // console.log(testimonial_div.style.width)
            // if(i<3){
            //     testimonial_div.setAttribute('class','testimonial_items-active')
            // }
        }
    // console.log(result)
    // console.log(typeof(result))
}).catch(error=>{
    // console.log(error)
})


let slideIterator = 0;
let nextIterator = 0;
function moveToNext(){
    // console.log("nextIterator",nextIterator);
    // console.log("slideIterator",slideIterator);
    if(nextIterator >=0){
        --nextIterator;
        const slideItem = document.querySelector('.testimonial_items');
        // console.log("moveToNext",slideItem.offsetWidth * nextIterator);
        let testimonials=document.getElementById('testimonials__slides')
        testimonials.style.transform = `translateX(${-slideItem.offsetWidth * nextIterator}px)`;
    }
    // else {
    //     te stimonials.style.transform = `translateX(0px)`;
    // }
}

function moveToPrevious()
{ 
    // console.log("slideIteratormoveToPrevious",slideIterator);
const slideItem = document.querySelector('.testimonial_items');

    if(slideIterator <7 ){
    slideIterator++;
    nextIterator = slideIterator;
    let testimonials=document.getElementById('testimonials__slides')
    testimonials.style.transform = `translateX(${-slideItem.offsetWidth * slideIterator}px)`;
    // console.log("widthtoprev",(-slideItem.offsetWidth * slideIterator));
}else{
    slideIterator = 0;
    testimonials.style.transform = `translateX(${-slideItem.offsetWidth*1}px)`;
}
}
function moveToTop(){
    window.scroll({
        top: 0, 
        left: 0, 
        behavior: 'smooth'
        });
}
//                       ***********login-path**********
// let tailoring_service=document.getElementById('tailoring-service')
// let tailor_send_btn=document.getElementById('tailor-send-btn')
// let changing_part=document.getElementById('changing-part')
let tailor=document.getElementById('tailor')
// console.log('====================================');
// console.log(tailor);
// console.log('====================================');
let customer=document.getElementById('customer')
let tailorname=document.getElementById('tailoring-service').name
let pass=document.getElementsByClassName('pass')
// console.log(pass[0])
// console.log(changing_part)
function TailorSection(){
    let block_box_chng=document.getElementById('block-box-chng')
    // block_box_chng.setAttribute('id','changingblock')
    // console.log(pass[0])
    // tailorname=tailorname
    // tailoring_service.removeAttribute('customer-send-btn')
    // tailoring_service.setAttribute('id','tailor-send-btn')
    pass[0].style.width='24.5rem'
    tailor.style.backgroundColor='#6F6F6F'
    customer.style.background='white'
    customer.style.color='#6f6f6f'
    tailor.style.color='white'
    customer.style.border=' 1px solid #6f6f6f'
    // changing_part.style.visibility='visible'
}
function customerSection(){
    // console.log(changing_part)
    pass[0].style.width='53rem'
    // tailorname=customername
    // tailoring_service.removeAttribute('tailor_send_btn')
    // tailoring_service.setAttribute('id','customer-send-btn')
    tailor.style.backgroundColor='white'
    customer.style.background='#6f6f6f'
    customer.style.color='white'
    tailor.style.color='#6f6f6f'
    tailor.style.border=' 1px solid #6f6f6f'
    // changing_part.style.visibility='hidden'
}