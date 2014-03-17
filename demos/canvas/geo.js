var Geo = function(canvas,options) {
  if (typeof(options) === "undefined") {
     options = {}
  }
  if (typeof(options.maxcolor) === "undefined") {
     options.maxcolor = 200;
  }
  var opt = options;
  var myCanvas = canvas;
  var ctx=myCanvas.getContext("2d");
  var theme = 'classic';
  var points = [];
  function drawPoint(x,y,r,i) {
    points.push([x,y,r,i]);
    ctx.globalCompositeOperation = "lighter";
    var radialGradient = ctx.createRadialGradient(x, y, i, x, y, r);
    radialGradient.addColorStop(0, 'rgba(' + opt.maxcolor + "," + opt.maxcolor + "," + opt.maxcolor + ',0.99)');
    radialGradient.addColorStop(1, 'rgba(0,0,0,0.99)');
    ctx.beginPath();
    ctx.arc(x, y, r, 0, 2 * Math.PI, false);
    ctx.fillStyle = radialGradient;
    ctx.fill();
  }

  function clear() {
    var ctx=myCanvas.getContext("2d");
    ctx.clearRect(0,0,myCanvas.width,myCanvas.height);
    points = [];
  }

  function clearColor() {
    ctx.clearRect(0,0,myCanvas.width,myCanvas.height);
    var oldpoints = points;
    points = [];
    for (var i=0; i< oldpoints.length;i++) {
       p = oldpoints[i]; 
       drawPoint(p[0],p[1],p[2],p[3]);
    }
  }


  function colorize() {
    var imgd = ctx.getImageData(0, 0, myCanvas.width, myCanvas.height);
    var pix = imgd.data;
    for (var i = 0, n = pix.length; i < n; i += 4) {
      r = pix[i ];
      g = pix[i+1];
      b = pix[i+2];
      a = pix[i+3];
      if (a == 1) {
        continue;
      }
      score = luminance(r,g,b)
      col = COLORTHEME[theme][255-score];
      pix[i] = col[0]
      pix[i+1] = col[1]
      pix[i+2] = col[2] 
    }
    ctx.putImageData(imgd, 0, 0);
  }

  function luminance(r,g,b) {
    // CCIR601 approximation 
    return Math.round((r + r + b + g + g+ g)/6);
  }

  function changeTheme(t) {
    theme = t;
  }
  return {drawPoint:drawPoint,
          clear: clear,
          clearColor: clearColor,
          colorize: colorize,
          changeTheme: changeTheme};
}
  
