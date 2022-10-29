console.log("********* INITIALISATION *********");

let sumIfOne = 0;

function countGroupOfSix() {
    let monTableau = [];
    for (let i = 0; i < 100; i++) {
        monTableau.push(Math.floor(Math.random() * 2));
    }

    let groupOfSix = 0;
    for (let j = 0; j < monTableau.length - 10; j++) {
        let nbSix = 0;
        if (monTableau[j] == 1) {
            nbSix++;

            let counter = 1;
            while (nbSix != 6 || counter != 6) {
                if (monTableau[j + counter] == 1) {
                    nbSix++;
                }
                if (monTableau[j + counter] == 0) {
                    break;
                }
                counter++;
            }
            if (nbSix == 6) {
                groupOfSix++;
                j += 5;
            }
        }
    }
    sumIfOne += groupOfSix;
}

let nbLoop = 100000;
for (let i = 0; i < nbLoop; i++) {
    countGroupOfSix();
}
let proba = sumIfOne / nbLoop;
console.log(proba);
