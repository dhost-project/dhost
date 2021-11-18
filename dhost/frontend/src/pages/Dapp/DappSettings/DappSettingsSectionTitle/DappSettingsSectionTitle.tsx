function DappSettingsSectionTitle(
   props: {_name: string, _description: string}
  ): React.ReactElement {


  return (

              <div className="ml-0 w-1/3">
                <h1 className="text-lg">{props._name}</h1>
                <a className="text-gray-500">{props._description}</a>
              </div>
  )

}

export default DappSettingsSectionTitle
