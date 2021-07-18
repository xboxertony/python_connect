class Item extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        const { word } = this.props;
        return <p className="word_decorate"><i className='fas fa-clipboard'></i>{word}</p>
    }
}
class Mention extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            0: "退款請由會員中心進入後，從歷史訂單旁的退款鈕進行退款",
            1: "退款皆全額退款",
            2: "出發時間三天內的訂單不得退款"
        };
    }
    make_array() {
        let arr = [];
        for (let i = 0; i < Object.keys(this.state).length; i++) {
            arr.push(<Item word={this.state[i]} key={this.state[i]} />);
        }
        arr.push(<a href='https://www.taipei-attraction.com/member_center'>連結會員中心</a>)
        arr.push(<div className='clear'></div>)
        return arr;
    }
    render() {
        return this.make_array()
    }
}