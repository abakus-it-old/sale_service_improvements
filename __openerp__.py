{
    'name': "Create task on SO improvements",
    'version': '1.0',
    'depends': ['sale_service',],
    'author': "Bernard DELHEZ, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Human Resource',
    'description': """
    Create task on SO improvements
    
    - It adds the field initial planned hours to the products. This field will be used to set the initial planned hours in the task. The computation of this field is:  initial planned hours (of the product) * product quantity (of the sale order line of the product.
    - It changes the name of the created task in: 'product name': 'sale order reference/description' ('sale order name')

    
    This module has been developed by Bernard Delhez, intern @ AbAKUS it-solutions.""",
    'data': ['view/product_template_view.xml',
             ],
}
