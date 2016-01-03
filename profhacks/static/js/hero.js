var pattern;

redraw();

window.onresize = function() {
    redraw();
};

function redraw() {
    console.log('redraw');
    pattern = Trianglify({
        height: height(),
        width: width(),
        cell_size: 30,
        seed: 'ufamx',
        x_colors: 'PRGn'});
    pattern.canvas(document.getElementById('hero_canvas'));
 }

function height() {
    return window.innerHeight;
}
 
function width() {
    return window.innerWidth;
}