var pattern;

redraw();

window.onresize = function() {
    redraw();
};

function redraw() {
//    console.log('redraw');
    var paired2 = ["#a6cee3", "#1f78b4", "b2df8a", "#33a02c", "#fb9a99", "#e31a1c", "#cab2d6", "#fdbf6f", "#ff7f00",];
    pattern = Trianglify({
        height: height(),
        width: width(),
        cell_size: 120,
        seed: 'ufamx',
        x_colors: paired2});
    pattern.canvas(document.getElementById('hero_canvas'));
 }

function height() {
    return window.innerHeight+180;
}
 
function width() {
    return window.innerWidth;
}