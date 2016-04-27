
export class Category {
    id: number
    name: string
}

export class Card {
    id: number
    category: Category
    first: string
    second: string
}
