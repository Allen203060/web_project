let availableKeywords = [
    'Advanced Engineering Mathematics',
    'Engineering Mathematics,Edition 2015, Oxford University Press',
    'Introduction to Artificial Intelligence & Expert Systems' ,
    'Artificial Intelligence',
    'The Complete Reference HTML & XHTML 5th Edition, Tata McGraw-Hill Company Limited',
    'HTML 4.0 by E. Stephen Mack, Janan Platt, Anaya Multimedia publication' ,
    'Web Enabled Commercial Application Development using HTML, JavaScript, DHTML and PHP by Ivan Bayross, 4th Edition, BPB Publications',
    'Fear the Flames',
    'Rise of the Night',
    'Scouraged',
    'Trapped',
    'Bury Me',
    'Dark Invasion',
    'A Land Divided',
    'Shade of Ruin' ,
    'A HARP in the STARS',
    'The Bell Jar by Sylvia Plath',
    'Greatest collections of Edgar Allan Poe',
    'If Birds Gather Your Hair',
    'The Weight Of The Soul',
    'Your Crib my Qibla',
    'Complete Works of Thomas chatterton',
    'Cruel Lies',
    'Find me in the rain',
    'It starts with us',
    'It ends with us',
    'King of Wrath',
    'King of Pride',
    'King of Greed',
    'King of Sloth',
    'Twisted Love',
    'Demonic Dolls',
    'Haunting of Abram Mansion',
    'Skin Curse',
    'Splintered',
    'Devil Next Door',
    'The Eye Thief',
    'The Girl With No Name',
    'The Horsea Marina Murders',
    'Dark psychology',
    'Criminal psychology',
    'The Book of Ethics of Bar Hebraeus',
    'Offensive and defensive cyber security strategies',
    'Inside Job',
    '24 hours that changed the World',
    'Computational Intelligent Techniques in Mechatronics',
    'Business Idioms',
    'Asterix and the falling sky',
    'Asterix and the Golden Sickle',
    'Asterix the legionary',
    'DEATH NOTE',
    'demon slayer volume 1',
    'Jujutsu Kaisen',
    'DC comic limited edition<br>DC marvel',
    'Harry Potter and the Philosephers stone',
    "Harry Potter and the chamber's of secret",
    'Harry Potter and the Prisoner of Azkaban',
    'Harry Potter and the Goblet Of Fire',
    'Harry Potter and the Order of Phoenix',
    'Harry Potter and the Half Blood Prince',
    'Harry Potter and the Deathly Hallows',
    'Harry Potter and the Cursed Child',
    'Harry Potter Series Entire Collection'
];
const resultsBox = document.querySelector(".result-box");
const inputBox = document.getElementById("input-box");
inputBox.onkeyup = function(){
    let result=[];
    let input = inputBox.value;
    if(input.length){
        result = availableKeywords.filter((keyword)=>{
            return keyword.toLowerCase().includes(input.toLowerCase());
        });
        console.log(result);
    }
    display(result);
    if(!result.length){
        resultsBox.innerHTML = '';
    }
}
function display(result){
    const content = result.map((list)=>{
        return "<li onclick=selectInput(this)>" + list + "</li>";
    });
    resultsBox.innerHTML = "<ul>"+ content.join('') + "</ul>";
}
function selectInput(list){
    inputBox.value = list.innerHTML;
    resultsBox.innerHTML = '';
}