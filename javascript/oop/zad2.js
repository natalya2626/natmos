
function doWelcome() {
    return "Hello";
    
}

console.log(doWelcome());


// 2. Напиши функцию, которая принимает имя пользователя и
//  возвращает новую строку с персональным приветствием.

function getUserWelcome(name) {
    return `Hello ${name}`;  // шаблонный литерал 
}

console.log(getUserWelcome("Nata"));


// 3. Напиши функцию, которая принимает текущий год и год рождения,
//  а затем вычисляет и возвращает возраст.

function getAge(currentYear, yearBirth) {
    return currentYear - yearBirth;
}

console.log(getAge(2026, 2000));

// 4. Напиши функцию, которая принимает два числа и возвращает 
// результат вычитания второго из первого.

function Subtract(number1, number2) {
    return number2 - number1;
}

console.log(Subtract(879, 545));
console.log(Subtract(345, 878));

// 5. Напиши функцию, которая принимает одно число, 
// умножает его само на себя и возвращает этот результат.

function multiply(number1) {
    return number1 * number1;
}

console.log(multiply(5));


// 6. Напиши функцию, которая принимает отдельные строки с именем
//  и фамилией, а возвращает их склеенными в одну строку через пробел.

function glue(name, surname) {
    return name + surname;
}

console.log(glue("nata", "ivano"));



// 7. Напиши функцию, которая принимает любое логическое значение и 
// возвращает строго противоположное ему.

function invert(value) {
    return !value;
}

console.log(invert(true));


// 8. Напиши функцию, которая принимает число и через условие
//  возвращает истину, если оно больше нуля, и ложь в противном случае.

function (number) {
    if (number > 0) {
        return true;
    }
    else 
        return false;
}


