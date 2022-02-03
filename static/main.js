const canvas = document.getElementById("canvas")
canvas.height = window.innerHeight
canvas.width = window.innerWidth

const ctx = canvas.getContext("2d")

let prevX = null
let prevY = null
let = draw = false

ctx.lineWidth = 12

// clear screen
let clearBtn = document.querySelector(".clear")
clearBtn.addEventListener("click", () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height)
})

// save image as png
//let saveBtn = document.querySelector(".save")
//saveBtn.addEventListener("click", () => {
 //   let data = canvas.toDataURL("imag/png")
  //  var img = document.getElementById("image").src = data;
  //  let a = document.createElement("a")
  //  console.log(data)
  //  a.href = data
  //  a.download = "sketch.png"
  //  a.click()
//})

function saveBtn() {
    var canvas = document.getElementById('canvas')
    document.getElementById('inp_img').value = canvas.toDataURL()
}


// toggle drawing
window.addEventListener("mousedown", (e) => draw = true)
window.addEventListener("mouseup", (e) => draw = false)

// draw lines
window.addEventListener("mousemove", (e) => {
    if(prevX == null || prevY == null){
        // Set the previous mouse positions to the current mouse positions
        prevX = e.clientX
        prevY = e.clientY
        return
    }
    let currentX = e.clientX
    let currentY = e.clientY

    if (draw == true) {
        ctx.beginPath()
        ctx.moveTo(prevX, prevY)
        ctx.lineTo(currentX, currentY)
        ctx.stroke()
    }

    prevX = currentX
    prevY = currentY
})