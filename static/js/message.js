class Messagelist extends React.Component{
    render(){
        const {content} = this.props
        return <p className='mes_list'><i className="fas fa-comments"></i>{content}</p>
    }
}

class Message extends React.Component{
    state = {
        0:"每個景點底下都可留言及評價",
        1:"其中評價方面，同一人會取最新的評價納入總平均",
        2:"每則留言都可貼多則景點圖",
        3:"留言中的圖會呈列在照片牆中",
        4:"圖片隨時皆可刪除"
    }
    render(){
        const {state} = this
        console.log(state)
        let arr = []
        for(let [key,val] of Object.entries(state)){
            arr.push(<Messagelist content={val} />)
        }
        console.log(arr)
        return arr
    }
}