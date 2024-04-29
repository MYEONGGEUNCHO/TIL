function func2 () {
    console.log('func2 호출');
};

function func3 () {
    console.log('test2.js에 있는 func3 호출');
};

export default () => {
    console.log('화살표 함수 호출')
};

export {func2, func3}