import {Router} from 'angular2/router'
import {Component, OnInit} from 'angular2/core'
import {CardService} from './card.service'
import {Card} from './card'
import {CardDetailComponent} from './card-detail.component'

@Component({
    selector: 'cards',
    template: `
        <h1>{{title}}</h1>
	<hr/>
	<ul class="cards">
        <li *ngFor="#card of cards"
            (click)="gotoCard(card)">
	<span class="badge">{{card.category.name}}</span> - {{card.first}}
        </li>
	</ul>
	<hr/>
        `,
    styles:[`
  .selected {
    background-color: #CFD8DC !important;
    color: white;
  }
  .cards {
    margin: 0 0 2em 0;
    list-style-type: none;
    padding: 0;
    width: 15em;
  }
  .cards li {
    cursor: pointer;
    position: relative;
    left: 0;
    background-color: #EEE;
    margin: .5em;
    padding: .3em 0;
    height: 1.6em;
    border-radius: 4px;
  }
  .cards li.selected:hover {
    background-color: #BBD8DC !important;
    color: white;
  }
  .cards li:hover {
    color: #607D8B;
    background-color: #DDD;
    left: .1em;
  }
  .cards .text {
    position: relative;
    top: -3px;
  }
  .cards .badge {
    display: inline-block;
    font-size: small;
    color: white;
    padding: 0.8em 0.7em 0 0.7em;
    background-color: #607D8B;
    line-height: 1em;
    position: relative;
    left: -1px;
    top: -4px;
    height: 1.8em;
    margin-right: .8em;
    border-radius: 4px 0 0 4px;
  }
	    `]
})

export class CardsComponent implements OnInit {
    ngOnInit() {
	this.getCards();
    }
    constructor(
	private _cardService: CardService,
	private _router: Router){
    }
    title = 'Latest additions'
    cards: Card[]
    gotoCard(card: Card) {
	let link = ['Card', {id: card.id}]
	this._router.navigate(link)
    }
    getCards() {
	this._cardService.getCardsSlowly().then(cards => this.cards = cards)
    }
}

