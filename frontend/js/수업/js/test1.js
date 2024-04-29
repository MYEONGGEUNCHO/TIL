function func1 () {
    console.log('func1 호출');
};

function func3 () {
    console.log('test1.js에 있는 func3 호출');
};

function temp () {
    console.log('func1에서 실행');
};

export {func1, func3};